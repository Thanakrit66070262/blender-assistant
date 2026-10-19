# eval/run_eval.py
import json
import os
import sys
from pathlib import Path

# ชี้ path ไปที่ src/
sys.path.append(str(Path(__file__).resolve().parent.parent / "src"))

from tools import check_python_syntax
from rag import BpyVectorStore
from generator import generate_bpy_solution, client

def run_evaluation(eval_path: str, vector_store: BpyVectorStore, top_k: int = 3, min_score: float = 0.40):
    with open(eval_path, "r", encoding="utf-8") as f:
        test_cases = json.load(f)

    total = len(test_cases)
    retrieval_hits = 0
    syntax_passes = 0
    api_matches = 0

    detailed_results = []
    failure_cases = []

    print(f"Starting evaluation on {total} test cases...\n")

    for idx, item in enumerate(test_cases, 1):
        q_id = item["id"]
        query = item["query"]
        gt_doc = item["ground_truth_doc_id"]
        expected_apis = item["expected_apis"]

        # 1. ทดสอบ Retrieval
        retrieved = vector_store.retrieve(query, top_k=top_k, min_score=min_score)
        retrieved_ids = [doc.doc_id for doc in retrieved]
        
        hit = gt_doc in retrieved_ids
        if hit:
            retrieval_hits += 1

        # 2. ทดสอบ Generation + Schema Validation
        syntax_valid = False
        api_match = False
        error_msg = None
        generated_code = ""

        try:
            res = generate_bpy_solution(query, retrieved)
            generated_code = res.code

            # ตรวจสอบ Syntax ผ่าน AST
            syntax_res = check_python_syntax(generated_code)
            syntax_valid = syntax_res["valid"]
            if syntax_valid:
                syntax_passes += 1

            # ตรวจสอบว่ามี API สำคัญครบหรือไม่
            api_match = any(api in generated_code for api in expected_apis)
            if api_match:
                api_matches += 1

        except Exception as e:
            error_msg = str(e)

        # บันทึกกรณีที่เกิดข้อผิดพลาดไว้เขียนในรายงาน (Failure Case Analysis)
        if not hit or not syntax_valid or not api_match:
            failure_cases.append({
                "id": q_id,
                "query": query,
                "retrieval_hit": hit,
                "syntax_valid": syntax_valid,
                "api_match": api_match,
                "error": error_msg,
                "code_snippet": generated_code[:120] if generated_code else ""
            })

        print(f"[{idx}/{total}] {q_id} | Retrieval: {'✓' if hit else '✗'} | Syntax: {'✓' if syntax_valid else '✗'} | API: {'✓' if api_match else '✗'}")

    summary = {
        "total_cases": total,
        "retrieval_hit_rate": f"{(retrieval_hits / total) * 100:.2f}%",
        "syntax_pass_rate": f"{(syntax_passes / total) * 100:.2f}%",
        "api_match_rate": f"{(api_matches / total) * 100:.2f}%",
        "failures_count": len(failure_cases)
    }

    # บันทึกผลลัพธ์ลงไฟล์เพื่อใช้เขียนรายงาน
    out_dir = Path("eval/results")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "eval_summary.json", "w", encoding="utf-8") as f:
        json.dump({"summary": summary, "failures": failure_cases}, f, indent=2, ensure_ascii=False)

    print("\n--- Evaluation Summary ---")
    print(json.dumps(summary, indent=2))
    return summary

if __name__ == "__main__":
    store = BpyVectorStore(client=client)
    loaded = store.load_index("data/vector_store.npz", "data/chunks.json")
    if not loaded:
        print("Error: Could not load index cache. Please run scripts/build_index.py first.")
        sys.exit(1)

    eval_file = Path("data/eval_set.json")
    run_evaluation(str(eval_file), store)