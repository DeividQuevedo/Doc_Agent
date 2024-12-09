import numpy as np

class VectorStore:
    def __init__(self):
        self.store = {}

    def add_vector(self, doc_id, vector):
        self.store[doc_id] = np.array(vector)

    def search(self, query_vector):
        query = np.array(query_vector)
        similarities = {doc_id: np.dot(query, vec) for doc_id, vec in self.store.items()}
        return sorted(similarities.items(), key=lambda x: x[1], reverse=True)
