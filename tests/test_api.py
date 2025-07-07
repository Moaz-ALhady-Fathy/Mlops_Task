import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the MLOps Model Serving API"}

def test_predict():
    response = client.post("/predict", json={"data": [1, 2, 3]})
    assert response.status_code == 200
    assert "prediction" in response.json()