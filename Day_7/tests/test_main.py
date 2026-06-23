from fastapi.testclient import TestClient
from Day_7.main import app

client = TestClient(app)

def test_create_user():
    r = client.post("/users", 
        json = {
            "username": "alice",
            "email":    "alice@test.com",
            "password": "secret123",
            "role" : "admin"
        }
    )
    assert r.status_code == 201
    assert r.json()["username"] == "alice"

def test_login():
    r = client.post("/auth/login", 
        data = {
            "username": "alice",
            "password": "secret123",
        }
    )
    assert r.status_code == 200
    assert "access_token" in r.json()
    
def _login(username, password) -> str:
    r = client.post("/auth/login", 
        data = {
            "username": username, 
            "password": password
        }
    )
    return r.json()["access_token"]

def test_create_post():
    token = _login("alice", "secret123")
    r = client.post("/posts/",
        json = {
            "title": "My First Post",
            "content": "Hello World",
            "category": "general",
            "published": True,
            "author_id": 1
        },
        headers = {
            "Authorization": f"Bearer {token}"
        }
    )
    assert r.status_code == 201
    assert r.json()["title"] == "My First Post"

def test_delete_post_admin():
    token = _login("alice", "secret123")
    r = client.delete("/posts/6",
        headers = {
            "Authorization": f"Bearer {token}"
        }
    )
    assert r.status_code == 204