import pytest
from fastapi.testclient import TestClient
from backend.src.main import app  # Replace with actual app import

client = TestClient(app)

def test_upload_post_contract():
    response = client.post("/api/upload", files={"file": ("test.pdf", b"%PDF-1.4 test content")})
    assert response.status_code == 200
    assert "file_id" in response.json()
