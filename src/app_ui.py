import sys
from pathlib import Path
import streamlit as st

# ตั้งค่า Path ให้เห็นโฟลเดอร์ src
root_dir = Path(__file__).resolve().parent.parent
src_dir = Path(__file__).resolve().parent
for p in [str(root_dir), str(src_dir)]:
    if p not in sys.path:
        sys.path.insert(0, p)

from rag import BpyVectorStore
from generator import client
from agent import BpyAgent

st.set_page_config(page_title="Blender Python Assistant", page_icon="🧊", layout="wide")
st.title("Blender Python (bpy) Scripting Assistant")
st.caption("RAG-Augmented Agentic Workflow powered by Gemma-4 & BGE-M3")

@st.cache_resource
def load_agent():
    store = BpyVectorStore(client=client)
    store.load_index("data/vector_store.npz", "data/chunks.json")
    return BpyAgent(client=client, vector_store=store, max_iterations=5)

agent = load_agent()

query = st.text_input("Enter your Blender task:", "Create a UV sphere with radius 2.0 at position (0, 0, 5)")

if st.button("Generate Script", type="primary"):
    with st.spinner("Agent is reasoning and executing tools..."):
        result = agent.run(query)
    
    st.subheader("Generated Script")
    st.code(result.get("final_output", ""), language="python")
    
    with st.expander("Agent Execution Trace & Tool Calls"):
        st.json(result.get("trace", []))