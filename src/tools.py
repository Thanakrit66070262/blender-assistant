# src/tools.py
import ast
from typing import Dict, Any

def check_python_syntax(code: str) -> Dict[str, Any]:
    """ตรวจสอบ Syntax ของ Python code ด้วย AST"""
    try:
        tree = ast.parse(code)
        # ตรวจสอบเพิ่มเติมว่ามีการเรียกใช้ bpy หรือไม่
        has_bpy = any(
            isinstance(node, ast.Import) and any(n.name == 'bpy' for n in node.names) or
            isinstance(node, ast.ImportFrom) and node.module == 'bpy'
            for node in ast.walk(tree)
        )
        return {
            "valid": True,
            "has_bpy_import": has_bpy,
            "error": None
        }
    except SyntaxError as e:
        return {
            "valid": False,
            "has_bpy_import": False,
            "error": f"SyntaxError at line {e.lineno}: {e.msg}"
        }