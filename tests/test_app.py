from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Container World!"}

def test_add():
    response = client.get("/add?a=4&b=6")
    assert response.status_code == 200
    assert response.json() == {"result": 10}