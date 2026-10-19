# scripts/build_index.py
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "src"))

from ingest import load_doc_chunks
from rag import BpyVectorStore
from generator import client

def main():
    # 1. โหลด Chunks ทั้งหมด
    docs = load_doc_chunks("data/raw_docs")
    
    # 2. ส่งเข้า Vector Store เพื่อคำนวณ Embedding
    store = BpyVectorStore(client=client)
    store.build_index(docs)

    # 3. เซฟไฟล์เก็บไว้ใช้งาน
    store.save_index()

if __name__ == "__main__":
    main()