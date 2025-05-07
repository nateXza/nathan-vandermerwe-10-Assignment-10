import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_create_user():
    response = client.post(
        "/api/users",
        json={"username": "testuser", "email": "test@example.com"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "testuser"
    assert data["email"] == "test@example.com"
    assert "id" in data

def test_get_users():
    # First create a user
    client.post(
        "/api/users",
        json={"username": "testuser", "email": "test@example.com"}
    )
    
    response = client.get("/api/users")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_create_image():
    response = client.post(
        "/api/images",
        json={"filename": "test.jpg", "path": "/images/test.jpg"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["filename"] == "test.jpg"
    assert data["path"] == "/images/test.jpg"
    assert "id" in data

def test_get_images():
    # First create an image
    client.post(
        "/api/images",
        json={"filename": "test.jpg", "path": "/images/test.jpg"}
    )
    
    response = client.get("/api/images")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_create_prediction():
    response = client.post(
        "/api/predictions",
        json={"result": "positive"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["result"] == "positive"
    assert "id" in data

def test_get_predictions():
    # First create a prediction
    client.post(
        "/api/predictions",
        json={"result": "positive"}
    )
    
    response = client.get("/api/predictions")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_invalid_user_creation():
    response = client.post(
        "/api/users",
        json={"username": "", "email": ""}
    )
    assert response.status_code == 400

def test_invalid_image_creation():
    response = client.post(
        "/api/images",
        json={"filename": "", "path": ""}
    )
    assert response.status_code == 400

def test_invalid_prediction_creation():
    response = client.post(
        "/api/predictions",
        json={"result": ""}
    )
    assert response.status_code == 400 