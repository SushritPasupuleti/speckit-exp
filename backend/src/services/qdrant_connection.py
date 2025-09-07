from qdrant_client import QdrantClient

class QdrantConnection:
    def __init__(self):
        self.client = QdrantClient(host="localhost", port=6333)

    def is_connected(self):
        try:
            self.client.get_collections()
            return True
        except Exception as e:
            print(f"Connection error: {e}")
            return False
