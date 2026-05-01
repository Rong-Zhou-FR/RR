"""RAG service for style example retrieval."""
import math
from typing import List, Dict, Any
from app.core.style_manager import get_style_examples
from app.core.config import settings


def dot_product(a: List[float], b: List[float]) -> float:
    """Compute dot product of two vectors."""
    return sum(x * y for x, y in zip(a, b))


def magnitude(v: List[float]) -> float:
    """Compute magnitude of vector."""
    return math.sqrt(sum(x * x for x in v))


def cosine_similarity(a: List[float], b: List[float]) -> float:
    """Compute cosine similarity between two vectors."""
    return dot_product(a, b) / (magnitude(a) * magnitude(b) + 1e-8)


class StyleRAG:
    """RAG for retrieving relevant style examples based on user prompt."""

    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self.model_name = model_name
        self.index: Dict[str, List[Dict[str, Any]]] = {}
        self.embeddings: Dict[str, List[float]] = {}
        self._client = None

    async def initialize(self):
        """Build the index from style examples."""
        from huggingface_hub import InferenceClient

        self._client = InferenceClient(
            model=self.model_name,
            token=settings.hf_api_token,
        )

        # Build index for each scenario
        for scenario in ["tech_guides", "code_docs", "conversation"]:
            examples = get_style_examples(scenario)
            if not examples:
                continue

            # Generate embeddings for all examples
            self.index[scenario] = []
            for i, ex in enumerate(examples):
                embedding = await self._get_embedding(ex)
                self.index[scenario].append({
                    "text": ex,
                    "index": i,
                })
                self.embeddings[f"{scenario}:{i}"] = embedding

        print(f"RAG initialized with {sum(len(v) for v in self.index.values())} examples")

    async def _get_embedding(self, text: str) -> List[float]:
        """Get embedding for text using HF feature extraction."""
        result = self._client.feature_extraction(text)
        if isinstance(result, list):
            return result
        return list(result)

    async def retrieve(
        self, query: str, scenario: str, top_k: int = 3
    ) -> List[str]:
        """Retrieve top-k style examples relevant to the query."""
        if not self.index or scenario not in self.index:
            # Fallback to all examples
            return get_style_examples(scenario)[:top_k]

        # Embed the query
        query_embedding = await self._get_embedding(query)

        # Compute similarities
        similarities = []
        for item in self.index[scenario]:
            idx = item["index"]
            key = f"{scenario}:{idx}"
            if key in self.embeddings:
                sim = cosine_similarity(query_embedding, self.embeddings[key])
                similarities.append((item["text"], sim))

        # Sort by similarity and return top-k
        similarities.sort(key=lambda x: x[1], reverse=True)
        return [text for text, _ in similarities[:top_k]]


# Global instance
_rag_instance: StyleRAG | None = None


async def get_rag() -> StyleRAG:
    """Get or create RAG instance."""
    global _rag_instance
    if _rag_instance is None:
        _rag_instance = StyleRAG()
        await _rag_instance.initialize()
    return _rag_instance