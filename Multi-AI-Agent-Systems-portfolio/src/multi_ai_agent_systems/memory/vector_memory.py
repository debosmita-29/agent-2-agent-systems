from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from multi_ai_agent_systems.db.repository import Repository


class VectorMemory:
    """pgvector-ready memory abstraction with TF-IDF fallback for local portability."""

    def __init__(self, repository: Repository):
        self.repository = repository

    def add(self, namespace: str, key: str, value: str) -> dict:
        item = self.repository.add_memory(namespace=namespace, key=key, value=value)
        return {"id": item.id, "namespace": item.namespace, "key": item.key, "value": item.value}

    def search(self, query: str, namespace: str | None = None, top_k: int = 5) -> list[dict]:
        memories = self.repository.get_memory(namespace=namespace, limit=200)
        if not memories:
            return []

        corpus = [f"{m.key}\n{m.value}" for m in memories]
        vectorizer = TfidfVectorizer(stop_words="english")
        matrix = vectorizer.fit_transform(corpus + [query])
        scores = cosine_similarity(matrix[-1], matrix[:-1]).flatten()

        results = []
        for idx in scores.argsort()[::-1][:top_k]:
            if scores[idx] <= 0:
                continue
            m = memories[idx]
            results.append(
                {"id": m.id, "namespace": m.namespace, "key": m.key, "value": m.value, "score": float(scores[idx])}
            )
        return results
