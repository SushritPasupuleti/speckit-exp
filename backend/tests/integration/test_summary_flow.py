import pytest
from fastapi.testclient import TestClient
from backend.src.main import app  # Replace with actual app import

client = TestClient(app)

def test_summary_flow_integration():
    # Simulate file upload
    upload_response = client.post("/api/upload", files={"file": ("test.pdf", b"%PDF-1.4 test content")})
    assert upload_response.status_code == 200
    file_id = upload_response.json().get("file_id")
    assert file_id is not None

    # Simulate summarization
    summary_response = client.post("/api/qna", json={"file_id": file_id, "question": "Summarize the content."})
    assert summary_response.status_code == 200
    assert "answer" in summary_response.json()
