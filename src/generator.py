# src/generator.py ด้านบนสุด
import json
import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

# 1. จัดการ Path ให้มองเห็นโฟลเดอร์ src เสมอ
src_dir = Path(__file__).resolve().parent
if str(src_dir) not in sys.path:
    sys.path.insert(0, str(src_dir))

# 2. โหลด .env จาก root
root_dir = src_dir.parent
load_dotenv(dotenv_path=root_dir / ".env")

# 3. Import schemas (ใช้ try-except เพื่อรองรับทั้งสองแบบ)
try:
    from schemas import BpyScriptResponse
except ModuleNotFoundError:
    from src.schemas import BpyScriptResponse

client = OpenAI()

def generate_bpy_solution(query: str, retrieved_chunks: list) -> BpyScriptResponse:
    context_text = ""
    for c in retrieved_chunks:
        context_text += f"\n--- Source: {c.metadata.get('module', 'bpy')} | {c.doc_id} ---\n{c.content}\n"

    system_prompt = f"""You are an expert Blender Python (bpy) developer.
Your task is to generate working bpy code based strictly on the provided context documentation.
You must output a strictly valid JSON object matching this JSON Schema:
{json.dumps(BpyScriptResponse.model_json_schema(), indent=2)}

Rules:
1. Do not invent non-existent bpy APIs.
2. If context does not support answering, explain and provide the closest safe code.
3. Every citation must come directly from the provided source headers.
4. Output raw JSON only. No markdown formatting like ```json."""

    user_prompt = f"User Request: {query}\n\nDocumentation Context:\n{context_text}"

    # เรียกโมเดลตามโจทย์กำหนด: gemma-4-E4B-it และ temperature=0
    response = client.chat.completions.create(
        model="gemma-4-E4B-it",
        temperature=0.0,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )

    raw_output = response.choices[0].message.content.strip()

    if raw_output.startswith("```json"):
        raw_output = raw_output[7:]
    if raw_output.endswith("```"):
        raw_output = raw_output[:-3]
    raw_output = raw_output.strip()

    try:
        validated_data = BpyScriptResponse.model_validate_json(raw_output)
        return validated_data
    except ValidationError as e:
        print(f"[Schema Validation Error] {e}")
        raise e