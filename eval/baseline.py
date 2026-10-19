# eval/baseline.py
import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent / "src"))

from tools import check_python_syntax
from generator import client

def run_baseline(eval_path: str):
    with open(eval_path, "r", encoding="utf-8") as f:
        test_cases = json.load(f)

    total = len(test_cases)
    syntax_passes = 0
    api_matches = 0

    print("Running Zero-shot Baseline (No-RAG)...")

    for idx, item in enumerate(test_cases, 1):
        query = item["query"]
        expected_apis = item["expected_apis"]

        # เรียก LLM โดยไม่ส่งเอกสารอ้างอิง
        try:
            prompt = f"Write a Blender Python (bpy) script for: {query}\nProvide only executable python code inside ```python ```."
            res = client.chat.completions.create(
                model="gemma-4-E4B-it",
                temperature=0.0,
                messages=[{"role": "user", "content": prompt}]
            )
            raw = res.choices[0].message.content
            # สกัดโค้ด
            code = raw.split("```python")[-1].split("```")[0] if "```python" in raw else raw

            if check_python_syntax(code)["valid"]:
                syntax_passes += 1
            if any(api in code for api in expected_apis):
                api_matches += 1
        except Exception:
            pass

        print(f"[Baseline {idx}/{total}] Processed.")

    print("\n--- Baseline Results ---")
    print(f"Syntax Pass Rate: {(syntax_passes / total) * 100:.2f}%")
    print(f"API Match Rate: {(api_matches / total) * 100:.2f}%")

if __name__ == "__main__":
    run_baseline("data/eval_set.json")