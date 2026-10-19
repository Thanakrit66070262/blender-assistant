# scripts/test_agent.py
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent / "src"))

from generator import client
from rag import BpyVectorStore
from agent import BpyAgent

# 1. โหลด Index
store = BpyVectorStore(client=client)
store.load_index("data/vector_store.npz", "data/chunks.json")

# 2. เริ่มต้น Agent
agent = BpyAgent(client=client, vector_store=store, max_iterations=5)

# 3. ยิงคำสั่งทดสอบ
result = agent.run("Write a script to create a UV sphere with radius 2.0 at position (0, 0, 5)")
print("\n=== FINAL RESULT ===")
print(result["final_output"])