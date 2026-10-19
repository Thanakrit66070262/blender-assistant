import os
import re
import requests
from bs4 import BeautifulSoup
from pathlib import Path

DOC_URLS = [
    "https://docs.blender.org/api/current/bpy.ops.mesh.html",
    "https://docs.blender.org/api/current/bpy.ops.object.html",
    "https://docs.blender.org/api/current/bpy.ops.transform.html",
    "https://docs.blender.org/api/current/bpy.data.html",
    "https://docs.blender.org/api/current/bpy.types.Object.html",
    "https://docs.blender.org/api/current/bpy.types.ShaderNodeBsdfPrincipled.html",
    "https://docs.blender.org/api/current/bpy.types.ObjectModifiers.html",
    "https://docs.blender.org/api/current/bpy.types.RenderSettings.html",
    "https://docs.blender.org/api/current/bpy.types.Scene.html",
    "https://docs.blender.org/api/current/bpy.types.LayerObjects.html",
]

OUTPUT_DIR = Path("data/raw_docs")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

def clean_text(text: str) -> str:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return "\n".join(lines)

def extract_clean_doc_id(dt_tag) -> str:
    """ดึง doc_id ที่ถูกต้อง สะอาด และตัดคำว่า class หรือสัญลักษณ์ anchor ออก"""
    # 1. ลองหาจาก attribute id ใน dt หรือ span ข้างใน
    doc_id = dt_tag.get("id")
    if not doc_id:
        span = dt_tag.find("span", id=True)
        if span:
            doc_id = span.get("id")

    # 2. ถ้าไม่มี id ให้ดึงจาก text แล้ว regex หา pattern bpy.*
    if not doc_id:
        text = dt_tag.get_text()
        match = re.search(r"(bpy\.[a-zA-Z0-9_\.]+)", text)
        if match:
            doc_id = match.group(1)

    if doc_id:
        doc_id = doc_id.replace("¶", "").strip()
    return doc_id or ""

def scrape_blender_page(url: str):
    print(f"Fetching: {url}")
    try:
        response = requests.get(url, headers=HEADERS, timeout=20)
        response.raise_for_status()
    except Exception as e:
        print(f"❌ Error fetching {url}: {e}")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    api_entries = soup.find_all("dl", class_=lambda c: c and any(k in c for k in ["py", "function", "class", "method", "attribute"]))
    
    saved_count = 0
    for entry in api_entries:
        dt = entry.find("dt")
        dd = entry.find("dd")
        if not dt or not dd:
            continue

        doc_id = extract_clean_doc_id(dt)
        if not doc_id.startswith("bpy."):
            continue

        signature = clean_text(dt.get_text().replace("¶", ""))
        description = clean_text(dd.get_text().replace("¶", ""))

        # ป้องกันการบันทึกหากไม่มีเนื้อหาคำอธิบาย
        if not description:
            description = "No description provided."

        markdown_chunk = f"""# {doc_id}

## Signature
```python
{signature}
Description
{description}
"""
        safe_filename = re.sub(r'[\/*?:"<>|]', "_", doc_id) + ".md"
        target_file = OUTPUT_DIR / safe_filename
        with open(target_file, "w", encoding="utf-8") as f:
            f.write(markdown_chunk)
            saved_count += 1

    print(f"✓ Saved {saved_count} API docs from {url}")

if __name__ == "__main__":
    for url in DOC_URLS:
        scrape_blender_page(url)