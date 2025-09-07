import pytest
import time
from fastapi.testclient import TestClient
from backend.src.main import app  # Replace with actual app import

client = TestClient(app)

def test_upload_endpoint_performance():
    start_time = time.time()
    response = client.post("/api/upload", files={"file": ("test.pdf", b"%PDF-1.4 test content")})
    end_time = time.time()
    assert response.status_code == 200
    assert (end_time - start_time) < 0.2

def test_qna_endpoint_performance():
    start_time = time.time()
    response = client.post("/api/qna", json={"file_id": "12345", "question": "What is the summary?"})
    end_time = time.time()
    assert response.status_code == 200
    assert (end_time - start_time) < 0.2
