import pytest
from fastapi.testclient import TestClient
from backend.src.main import app  # Replace with actual app import

client = TestClient(app)

def test_qna_flow_integration():
    # Simulate file upload
    upload_response = client.post("/api/upload", files={"file": ("test.pdf", b"%PDF-1.4 test content")})
    assert upload_response.status_code == 200
    file_id = upload_response.json().get("file_id")
    assert file_id is not None

    # Simulate QnA
    qna_response = client.post("/api/qna", json={"file_id": file_id, "question": "What is the summary?"})
    assert qna_response.status_code == 200
    assert "answer" in qna_response.json()
