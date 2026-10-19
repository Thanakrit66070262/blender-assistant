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