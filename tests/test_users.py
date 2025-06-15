import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.services.user_service import UserService

def test_create_user(client: TestClient, db: Session):
    response = client.post(
        "/api/users/",
        json={
            "username": "testuser",
            "email": "test@example.com",
            "password": "testpassword"
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert data["username"] == "testuser"
    assert data["email"] == "test@example.com"
    assert "id" in data

def test_create_user_duplicate_email(client: TestClient, db: Session):
    # Create first user
    user_service = UserService(db)
    user_service.create_user(
        username="testuser1",
        email="test@example.com",
        password="testpassword"
    )
    
    # Try to create second user with same email
    response = client.post(
        "/api/users/",
        json={
            "username": "testuser2",
            "email": "test@example.com",
            "password": "testpassword"
        }
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Email already registered"

def test_login_user(client: TestClient, db: Session):
    # Create user
    user_service = UserService(db)
    user_service.create_user(
        username="testuser",
        email="test@example.com",
        password="testpassword"
    )
    
    # Login
    response = client.post(
        "/api/users/token",
        data={
            "username": "testuser",
            "password": "testpassword"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"
