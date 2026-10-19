# src/ingest.py
import re
from pathlib import Path
from typing import List, Dict, Any

def load_doc_chunks(raw_docs_dir: str = "data/raw_docs") -> List[Dict[str, Any]]:
    docs_path = Path(raw_docs_dir)
    chunks = []

    if not docs_path.exists():
        raise FileNotFoundError(f"Directory {raw_docs_dir} not found.")

    md_files = list(docs_path.glob("*.md"))
    if not md_files:
        print(f"Warning: No .md files found in {raw_docs_dir}")
        return []

    for file_path in md_files:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        content = content.strip()
        if not content:
            continue

        # 1. ดึง doc_id: ถ้าในไฟล์มี # bpy.xxx ให้ดึงมา ถ้าไม่มีให้ใช้ชื่อไฟล์ (ตัด .md ออก)
        lines = content.splitlines()
        first_line = lines[0].strip() if lines else ""
        
        if first_line.startswith("#"):
            # ตัดเครื่องหมาย # และช่องว่างออก
            doc_id = first_line.lstrip("#").strip()
            # ตัดคำว่า DOC_ID: ออกถ้ามี
            doc_id = re.sub(r"^DOC_ID:\s*", "", doc_id)
        else:
            doc_id = file_path.stem  # เช่น bpy.ops.mesh.attribute_set

        # 2. ทำความสะอาดตัวอักษร encoding เพี้ยนจากเว็บ
        clean_content = content.replace("Â", "").replace("â€“", "-")

        # 3. ระบุชื่อ module
        parts = doc_id.split(".")
        module_name = ".".join(parts[:3]) if len(parts) >= 3 else "bpy"

        chunks.append({
            "id": doc_id,
            "content": clean_content,
            "metadata": {
                "source_file": file_path.name,
                "module": module_name
            }
        })

    print(f"Loaded and chunked {len(chunks)} API documents.")
    return chunks