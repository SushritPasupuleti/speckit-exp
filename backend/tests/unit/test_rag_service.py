import pytest
from backend.src.services.rag_service import RAGService

@pytest.fixture
def rag_service():
    return RAGService(vector_db="MockDB")

def test_rag_service_retrieve_and_generate(rag_service):
    query = "Test query"
    response = rag_service.retrieve_and_generate(query)
    assert response == f"Simulated RAG response for query: {query}"
