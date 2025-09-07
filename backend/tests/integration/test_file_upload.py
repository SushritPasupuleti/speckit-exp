import pytest
from fastapi.testclient import TestClient
from backend.src.main import app  # Replace with actual app import

client = TestClient(app)

def test_file_upload_integration():
    response = client.post("/api/upload", files={"file": ("test.pdf", b"%PDF-1.4 test content")})
    assert response.status_code == 200
    file_id = response.json().get("file_id")
    assert file_id is not None
