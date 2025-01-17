from fastapi.testclient import TestClient
from main import app  # Importing your FastAPI app

client = TestClient(app)

# Test the root endpoint
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200  # Check for HTTP 200
    assert response.json() == {"message": "Welcome!"}  # Check the response payload
