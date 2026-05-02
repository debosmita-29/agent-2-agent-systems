from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from multi_ai_agent_systems.db.repository import Repository


class Retriever:
    def __init__(self, repository: Repository):
        self.repository = repository

    def search(self, query: str, top_k: int = 3) -> list[dict]:
        docs = self.repository.list_documents()
        if not docs:
            return []

        corpus = [f"{d.title}\n{d.content}" for d in docs]
        vectorizer = TfidfVectorizer(stop_words="english")
        matrix = vectorizer.fit_transform(corpus + [query])
        scores = cosine_similarity(matrix[-1], matrix[:-1]).flatten()

        results = []
        for idx in scores.argsort()[::-1][:top_k]:
            if scores[idx] <= 0:
                continue
            doc = docs[idx]
            results.append(
                {
                    "id": doc.id,
                    "title": doc.title,
                    "content": doc.content[:1000],
                    "source": doc.source,
                    "score": float(scores[idx]),
                }
            )
        return results
