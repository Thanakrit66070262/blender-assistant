import os
import json
import numpy as np
from pathlib import Path
from dataclasses import dataclass
from typing import List, Dict, Any
import time

@dataclass
class RetrievedChunk:
    doc_id: str
    content: str
    metadata: Dict[str, Any]
    score: float

# src/rag.py
class BpyVectorStore:
    def __init__(self, client, embedding_model: str = "bge-m3"):
        self.client = client
        self.embedding_model = embedding_model
        self.chunks: List[Dict[str, Any]] = []
        self.embeddings_matrix: np.ndarray = np.empty((0,))

    def get_embedding(self, text: str) -> List[float]:
        # ตัดความยาวไม่ให้ยาวเกิน limit ของ bge-m3
        truncated = text[:2000]
        response = self.client.embeddings.create(
            input=truncated,
            model=self.embedding_model
        )
        return response.data[0].embedding

    def build_index(self, documents: List[Dict[str, Any]], batch_size: int = 5):
        self.chunks = documents
        embeddings = []
        
        print(f"Generating embeddings for {len(documents)} chunks (batch_size={batch_size})...")
        
        for i in range(0, len(documents), batch_size):
            batch = documents[i:i + batch_size]
            # จำกัดความยาว chunk ป้องกันโมเดลรับไม่ไหว
            texts = [doc["content"][:2000] for doc in batch]
            
            # ทำ retry เล็กน้อยกรณี proxy connection error
            retries = 3
            success = False
            while retries > 0 and not success:
                try:
                    res = self.client.embeddings.create(
                        input=texts,
                        model=self.embedding_model
                    )
                    embeddings.extend([item.embedding for item in res.data])
                    success = True
                except Exception as e:
                    retries -= 1
                    print(f"Batch {i//batch_size + 1} failed: {e}. Retrying ({3 - retries}/3)...")
                    time.sleep(2)
            
            if not success:
                raise RuntimeError(f"Failed to generate embeddings for batch starting at index {i}")

            if (i // batch_size + 1) % 5 == 0 or i + batch_size >= len(documents):
                print(f"Processed {min(i + batch_size, len(documents))}/{len(documents)} chunks...")

        self.embeddings_matrix = np.array(embeddings)
        print("Vector index built successfully.")

    def save_index(self, index_path: str = "data/vector_store.npz", chunks_path: str = "data/chunks.json"):
        Path(index_path).parent.mkdir(parents=True, exist_ok=True)
        np.savez_compressed(index_path, embeddings=self.embeddings_matrix)
        with open(chunks_path, "w", encoding="utf-8") as f:
            json.dump(self.chunks, f, ensure_ascii=False, indent=2)
        print(f"Index cached at {index_path} and {chunks_path}")

    def load_index(self, index_path: str = "data/vector_store.npz", chunks_path: str = "data/chunks.json") -> bool:
        if not (Path(index_path).exists() and Path(chunks_path).exists()):
            return False
        
        data = np.load(index_path)
        self.embeddings_matrix = data["embeddings"]
        with open(chunks_path, "r", encoding="utf-8") as f:
            self.chunks = json.load(f)
        print(f"Loaded cached index with {len(self.chunks)} items.")
        return True

    def retrieve(self, query: str, top_k: int = 3, min_score: float = 0.40) -> List[RetrievedChunk]:
        if len(self.chunks) == 0:
            return []

        query_emb = np.array(self.get_embedding(query))
        norm_query = np.linalg.norm(query_emb)
        norm_matrix = np.linalg.norm(self.embeddings_matrix, axis=1)

        scores = np.dot(self.embeddings_matrix, query_emb) / (norm_matrix * norm_query)
        ranked_indices = np.argsort(scores)[::-1]

        results = []
        for idx in ranked_indices[:top_k]:
            score = float(scores[idx])
            if score >= min_score:
                doc = self.chunks[idx]
                results.append(RetrievedChunk(
                    doc_id=doc["id"],
                    content=doc["content"],
                    metadata=doc["metadata"],
                    score=score
                ))
        return results