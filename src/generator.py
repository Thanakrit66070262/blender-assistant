# src/generator.py
import json
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import ValidationError
from schemas import BpyScriptResponse

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)
# เรียก OpenAI() ว่างๆ ตามมาตรฐานคลาส ซึ่งจะอ่าน OPENAI_BASE_URL และ OPENAI_API_KEY
# จาก Environment Variables ให้อัตโนมัติ (เช่น ตอนรันผ่าน uv run --env-file .env หรือเซ็ต env ไว้)
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