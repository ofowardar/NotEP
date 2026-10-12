import pytest
from fastapi.testclient import TestClient
from main import app
from app.database import SessionLocal, Base, engine, get_db

def override_get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture(scope="function")
def db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def client(db):
    app.dependency_overrides[get_db] = override_get_db
    return TestClient(app)


class TestAuth:
    
    def test_register_success(self, client):
        """Başarılı register"""
        response = client.post("/auth/register", json={
            "email": "test@example.com",
            "password": "test123"
        })
        assert response.status_code == 201
        assert response.json()["email"] == "test@example.com"
    
    
    def test_register_duplicate_email(self, client):
        """Aynı email'e iki kez register"""
        client.post("/auth/register", json={
            "email": "test@example.com",
            "password": "test123"
        })
        response = client.post("/auth/register", json={
            "email": "test@example.com",
            "password": "test456"
        })
        assert response.status_code == 400
        assert "zaten kayıtlı" in response.json()["detail"]
    
    
    def test_login_success(self, client):
        """Başarılı login"""
        client.post("/auth/register", json={
            "email": "test@example.com",
            "password": "test123"
        })
        
        response = client.post("/auth/login", json={
            "email": "test@example.com",
            "password": "test123"
        })
        assert response.status_code == 200
        assert "access_token" in response.json()
        assert response.json()["token_type"] == "bearer"
    
    
    def test_login_wrong_password(self, client):
        """Yanlış şifre"""
        client.post("/auth/register", json={
            "email": "test@example.com",
            "password": "test123"
        })
        
        response = client.post("/auth/login", json={
            "email": "test@example.com",
            "password": "wrongpassword"
        })
        assert response.status_code == 401
        assert "Email veya şifre yanlış" in response.json()["detail"]
    
    
    def test_login_nonexistent_email(self, client):
        """Olmayan email'e login"""
        response = client.post("/auth/login", json={
            "email": "nonexistent@example.com",
            "password": "test123"
        })
        assert response.status_code == 401