import pytest
from fastapi.testclient import TestClient
from backend.src.main import app  # Replace with actual app import

client = TestClient(app)

def test_qna_post_contract():
    payload = {"file_id": "12345", "question": "What is the summary?"}
    response = client.post("/api/qna", json=payload)
    assert response.status_code == 200
    assert "answer" in response.json()
