from typing import List
from pydantic import BaseModel, Field

class Citation(BaseModel):
    source_title: str = Field(description="ชื่อเอกสารหรือ API endpoint ที่อ้างอิง")
    module: str = Field(description="โมดูลของ bpy เช่น bpy.ops.mesh, bpy.data")

class BpyScriptResponse(BaseModel):
    target_version: str = Field(
        description="เวอร์ชัน Blender ที่รองรับ เช่น 'Blender 4.x'",
        default="Blender 4.x"
    )
    code: str = Field(
        description="โค้ดสคริปต์ Python สำหรับ bpy ที่สมบูรณ์และถูกต้องตาม syntax"
    )
    explanation: str = Field(
        description="คำอธิบายการทำงานของโค้ดและ logic ในการเรียกใช้งาน API"
    )
    citations: List[Citation] = Field(
        description="รายการเอกสารที่ถูกนำมาใช้อ้างอิงจริงในสคริปต์",
        min_length=1
    )