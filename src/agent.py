# src/agent.py
import json
from typing import Dict, Any, List
from openai import OpenAI
from rag import BpyVectorStore
from tools import check_python_syntax

class BpyAgent:
    def __init__(self, client: OpenAI, vector_store: BpyVectorStore, max_iterations: int = 5):
        self.client = client
        self.vector_store = vector_store
        self.max_iterations = max_iterations

        # 1. กำหนด Tools Definition ตามมาตรฐาน OpenAI Tool Calling
        self.tools = [
            {
                "type": "function",
                "function": {
                    "name": "search_docs",
                    "description": "Search Blender Python (bpy) documentation for relevant APIs, operators, or properties.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "query": {
                                "type": "string",
                                "description": "Search query keyword, e.g. 'primitive uv sphere add' or 'mesh subdivide'"
                            }
                        },
                        "required": ["query"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "check_syntax",
                    "description": "Validate Python syntax using AST parser before producing final script.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "code": {
                                "type": "string",
                                "description": "The python code string to check"
                            }
                        },
                        "required": ["code"]
                    }
                }
            }
        ]

    def _execute_tool(self, name: str, args: Dict[str, Any]) -> str:
        if name == "search_docs":
            query = args.get("query", "")
            chunks = self.vector_store.retrieve(query, top_k=2, min_score=0.35)
            if not chunks:
                return "No relevant documentation found."
            results = []
            for c in chunks:
                results.append(f"Source ID: {c.doc_id}\nContent:\n{c.content}")
            return "\n---\n".join(results)

        elif name == "check_syntax":
            code = args.get("code", "")
            res = check_python_syntax(code)
            return json.dumps(res)

        return f"Tool {name} not found."

    def run(self, user_prompt: str) -> Dict[str, Any]:
        system_message = {
            "role": "system",
            "content": (
                "You are an expert Blender Python assistant. You have access to tools:\n"
                "- `search_docs`: to find exact bpy function signatures and parameters.\n"
                "- `check_syntax`: to check whether your generated Python script is syntactically valid.\n"
                "Solve the user request step-by-step. Before giving the final code, verify syntax if needed.\n"
                "When you are finished, output your final Python script cleanly inside ```python ... ```."
            )
        }

        messages = [
            system_message,
            {"role": "user", "content": user_prompt}
        ]

        iterations = 0
        execution_trace = []

        print(f"\n[Agent] Starting task: {user_prompt}")

        while iterations < self.max_iterations:
            iterations += 1
            print(f"[Agent Loop] Iteration {iterations}...")

            response = self.client.chat.completions.create(
                model="gemma-4-E4B-it",
                messages=messages,
                tools=self.tools,
                tool_choice="auto",
                temperature=0.0
            )

            msg = response.choices[0].message
            messages.append(msg)

            # ตรวจสอบว่าโมเดลต้องการเรียก Tool หรือไม่
            if msg.tool_calls:
                for tool_call in msg.tool_calls:
                    fn_name = tool_call.function.name
                    raw_args = tool_call.function.arguments
                    try:
                        args = json.loads(raw_args)
                    except json.JSONDecodeError:
                        args = {}

                    print(f"  -> Tool Call: {fn_name}({args})")
                    tool_output = self._execute_tool(fn_name, args)

                    execution_trace.append({
                        "iteration": iterations,
                        "tool": fn_name,
                        "args": args,
                        "output": tool_output[:100] + "..." if len(tool_output) > 100 else tool_output
                    })

                    # ส่งผลลัพธ์ Tool กลับเข้าไปในประวัติแชท
                    messages.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "name": fn_name,
                        "content": str(tool_output)
                    })
            else:
                # Stop Condition: โมเดลไม่เรียก Tool แล้ว และส่ง Final Response ออกมา
                final_content = msg.content or ""
                print(f"[Agent] Finished in {iterations} iterations (Stop condition met).")
                return {
                    "status": "success",
                    "iterations": iterations,
                    "final_output": final_content,
                    "trace": execution_trace
                }

        # Stop Condition: ครบ max_iterations
        print("[Agent] Reached maximum iterations.")
        return {
            "status": "max_iterations_reached",
            "iterations": iterations,
            "final_output": messages[-1].content if messages[-1].content else "",
            "trace": execution_trace
        }