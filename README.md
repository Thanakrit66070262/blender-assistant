Blender Python (bpy) Scripting Assistant

A developer assistant designed to generate, validate, and cite Blender Python (bpy) scripts. Built with gemma-4-E4B-it, dense retrieval via bge-m3, dynamic tool calling (Agentic ReAct loop), and static AST syntax verification.

Developed as a capstone project for Building LLM-Powered Applications (KMITL).

1. Features and Implemented Capabilities

RAG and Citations (Capability Family #2): Dense vector retrieval (bge-m3) across indexed Blender 4.x Python API Sphinx documentation with a strict min_score floor (0.40) to prevent irrelevant context injection.

Agent Loop with Tools (Capability Family #4): ReAct loop with explicit stopping conditions and fallback iterations. Dynamically queries documentation (search_docs) and runs syntax diagnostics (check_syntax).

AST Static Validation: Validates Python syntax using Python's native ast.parse prior to returning code to the user.

Structured Schema (Pydantic): Enforces structured JSON responses containing executable code, target version, explanation, and exact source citations.

Evaluation Harness (Capability Family #3): Built-in evaluation pipeline testing 30 real-world Blender scripting scenarios against a zero-shot baseline.

2. System Architecture

                      +-----------------------------+
                      |         User Query          |
                      +-----------------------------+
                                     |
                                     v
                      +-----------------------------+
                      |   BpyAgent (ReAct Loop)     |
                      |   Model: gemma-4-E4B-it     |
                      |   Max Iterations: 5         |
                      +-----------------------------+
                               /            \
          [Call: search_docs] /              \ [Call: check_syntax]
                             v                v
                 +-------------------+  +-------------------+
                 |  BpyVectorStore   |  | AST Syntax Engine |
                 |     (bge-m3)      |  |   (ast.parse)     |
                 +-------------------+  +-------------------+
                             \                /
                              v              v
                      +-----------------------------+
                      |    Pydantic Schema Output   |
                      |   (BpyScriptResponse)       |
                      +-----------------------------+
                                     |
                                     v
                      +-----------------------------+
                      |  Final Verified Code + Docs |
                      +-----------------------------+


3. Project Structure

blender-assistant/
├── data/
│   ├── raw_docs/              # Blender Sphinx documentation (Markdown)
│   ├── chunks.json            # Processed document chunks
│   ├── vector_store.npz       # Cached bge-m3 dense embeddings
│   └── eval_set.json          # 30 test cases across 7 categories
├── eval/
│   ├── baseline.py            # Zero-shot baseline evaluation script
│   ├── run_eval.py            # Complete evaluation harness
│   └── results/
│       └── eval_summary.json  # Stored quantitative metrics and failure logs
├── scripts/
│   ├── build_index.py         # Embedding ingestion and indexing pipeline
│   └── test_agent.py          # Standalone test runner for BpyAgent
├── src/
│   ├── agent.py               # ReAct Agent loop implementation
│   ├── generator.py           # LLM caller and proxy setup
│   ├── rag.py                 # Vector store and cosine similarity search
│   ├── schemas.py             # Pydantic structured output models
│   ├── tools.py               # AST syntax checker tool
│   └── main.py                # Interactive CLI entrypoint
├── .env.example               # Template for environment variables
├── .gitignore                 # Excludes keys, virtual environments, and caches
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation


4. Setup and Installation

Prerequisites

Python 3.10 - 3.13

Class Proxy credentials (OPENAI_BASE_URL and OPENAI_API_KEY)

Installation

git clone https://github.com/<your-username>/blender-assistant.git
cd blender-assistant

python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

pip install -r requirements.txt


Configuration

Create a .env file in the project root:

OPENAI_BASE_URL="https://your-proxy-endpoint/v1"
OPENAI_API_KEY="your-proxy-api-key"


5. Usage

Indexing Documentation

python scripts/build_index.py


Running Queries via CLI

python -m src.main "How to create a UV sphere with radius 2 at (0, 0, 5)?"
python -m src.main "Subdivide all selected faces once in Edit Mode"


6. Evaluation and Results

Evaluated on 30 test queries (data/eval_set.json) covering mesh creation, transforms, hierarchy, edit mode operations, shaders, modifiers, and rendering.

Quantitative Comparison

Metric

Baseline (Zero-Shot / No-RAG)

Proposed Pipeline (RAG + Agent)

Delta

Retrieval Hit Rate (Recall@3)

N/A

40.00% (12/30)

-

Syntax Pass Rate (ast.parse)

100.00% (30/30)

100.00% (30/30)

0.00%

API Match Rate

93.33% (28/30)

83.33% (25/30)

-10.00%

Reproduction Commands

# Run baseline:
python eval/baseline.py

# Run full evaluation:
python eval/run_eval.py


Failure Analysis

Retrieval Distraction Effect: The baseline model contains strong parametric memory for common bpy calls (93.33% match). In cases where dense retrieval yielded distractor chunks (Recall@3 = 40.00%), the model over-conditioned on tangential context, causing API keyword misses on 5 queries (bpy_06, bpy_17, bpy_18, bpy_25, bpy_26).

Corpus Scope Boundaries: Specific operators (such as bpy.ops.mesh.subdivide) were absent from the harvested documentation subset, forcing fallback behavior.

7. Submission Artifacts

Report: docs/report.pdf

Demo Video: [Insert Video URL here]