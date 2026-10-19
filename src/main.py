# src/main.py ด้านบนสุด
import sys
from pathlib import Path
from dotenv import load_dotenv

# เพิ่มทั้ง root และ src ลง sys.path
root_dir = Path(__file__).resolve().parent.parent
src_dir = Path(__file__).resolve().parent

for p in [str(root_dir), str(src_dir)]:
    if p not in sys.path:
        sys.path.insert(0, p)

load_dotenv(dotenv_path=root_dir / ".env")

# นำเข้าโมดูล
try:
    from rag import BpyVectorStore
    from schemas import BpyScriptResponse
    from generator import generate_bpy_solution, client
except ModuleNotFoundError:
    from src.rag import BpyVectorStore
    from src.schemas import BpyScriptResponse
    from src.generator import generate_bpy_solution, client

def answer_user_bpy_request(user_query: str, vector_store: BpyVectorStore):
    # 1. ค้นหาเอกสารที่เกี่ยวข้อง
    retrieved = vector_store.retrieve(user_query, top_k=3, min_score=0.40)
    
    if not retrieved:
        return {
            "status": "error",
            "message": "No relevant Blender documentation found meeting the min_score floor."
        }

    # 2. ส่งให้ LLM และแปลงเป็น Pydantic Object
    result: BpyScriptResponse = generate_bpy_solution(user_query, retrieved)

    # 3. นำผลลัพธ์ไปใช้งานต่อ (พร้อม Citations)
    return {
        "status": "success",
        "version": result.target_version,
        "script": result.code,
        "explanation": result.explanation,
        "citations": [c.model_dump() for c in result.citations]
    }

if __name__ == "__main__":
    # โหลดแคชเวกเตอร์
    store = BpyVectorStore(client=client)
    store.load_index("data/vector_store.npz", "data/chunks.json")

    # รับคำถามจาก Command Line Argument ถ้าไม่มีให้ใช้ค่าตั้งต้น
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
    else:
        query = "How to create a UV sphere with radius 2 at (0, 0, 5)?"

    print(f"\nProcessing Query: {query}\n" + "-"*40)
    response = answer_user_bpy_request(query, store)
    
    # แสดงผลให้อ่านง่าย
    if response["status"] == "success":
        print(f"Target Version: {response['version']}")
        print(f"Generated Script:\n{response['script']}")
        print(f"Explanation:\n{response['explanation']}")
        print(f"Citations: {response['citations']}")
    else:
        print(f"Error: {response['message']}")