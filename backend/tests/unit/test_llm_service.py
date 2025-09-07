import pytest
from backend.src.services.llm_service import LLMService

@pytest.fixture
def llm_service():
    return LLMService(llm_provider="MockProvider")

def test_llm_service_query(llm_service):
    prompt = "Test prompt"
    response = llm_service.query(prompt)
    assert response == f"Simulated response for prompt: {prompt}"
