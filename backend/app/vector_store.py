import numpy as np


class VectorStore:
    def __init__(self):
        self.chunks = []
        self.embeddings = []

    def add(self, chunks: list[str], embeddings: list[list[float]]):
        self.chunks.extend(chunks)
        self.embeddings.extend(embeddings)

    def search(self, query_embedding: list[float], top_k: int = 3):
        if not self.embeddings:
            return []

        query_vector = np.array(query_embedding)

        scores = []

        for chunk, embedding in zip(self.chunks, self.embeddings):
            vector = np.array(embedding)

            similarity = np.dot(query_vector, vector) / (
                np.linalg.norm(query_vector) * np.linalg.norm(vector)
            )

            scores.append((similarity, chunk))

        scores.sort(reverse=True, key=lambda item: item[0])

        return scores[:top_k]