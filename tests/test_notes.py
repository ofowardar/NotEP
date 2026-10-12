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


def get_token(client, email="test@example.com", password="test123"):
    """Helper: Register olup token al"""
    client.post("/auth/register", json={
        "email": email,
        "password": password
    })
    response = client.post("/auth/login", json={
        "email": email,
        "password": password
    })
    return response.json()["access_token"]


class TestNotes:
    
    def test_create_note_success(self, client):
        """Başarılı not oluşturma"""
        token = get_token(client)
        
        response = client.post(
            "/notes",
            json={"title": "Test", "content": "İçerik"},
            headers={"Authorization": f"Bearer {token}"}
        )
        assert response.status_code == 201
        assert response.json()["title"] == "Test"
    
    
    def test_create_note_without_token(self, client):
        """Token olmadan not oluşturamaz"""
        response = client.post(
            "/notes",
            json={"title": "Test", "content": "İçerik"}
        )
        assert response.status_code == 401
    
    
    def test_list_notes(self, client):
        """Notları listele"""
        token = get_token(client)
        
        client.post(
            "/notes",
            json={"title": "Note 1", "content": "İçerik 1"},
            headers={"Authorization": f"Bearer {token}"}
        )
        client.post(
            "/notes",
            json={"title": "Note 2", "content": "İçerik 2"},
            headers={"Authorization": f"Bearer {token}"}
        )
        
        response = client.get(
            "/notes",
            headers={"Authorization": f"Bearer {token}"}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["total"] == 2
        assert len(data["items"]) == 2
    
    
    def test_get_note_success(self, client):
        """Tekli not getir"""
        token = get_token(client)
        
        create_response = client.post(
            "/notes",
            json={"title": "Test", "content": "İçerik"},
            headers={"Authorization": f"Bearer {token}"}
        )
        note_id = create_response.json()["id"]
        
        response = client.get(
            f"/notes/{note_id}",
            headers={"Authorization": f"Bearer {token}"}
        )
        assert response.status_code == 200
        assert response.json()["title"] == "Test"
    
    
    def test_delete_note_success(self, client):
        """Notu sil"""
        token = get_token(client)
        
        create_response = client.post(
            "/notes",
            json={"title": "Test", "content": "İçerik"},
            headers={"Authorization": f"Bearer {token}"}
        )
        note_id = create_response.json()["id"]
        
        response = client.delete(
            f"/notes/{note_id}",
            headers={"Authorization": f"Bearer {token}"}
        )
        assert response.status_code == 204
        
        get_response = client.get(
            f"/notes/{note_id}",
            headers={"Authorization": f"Bearer {token}"}
        )
        assert get_response.status_code == 404