from fastapi.testclient import TestClient
from app.main import app
import random

client = TestClient(app)

def random_email():
    return f"test{random.randint(1, 10000)}@example.com"

def test_signup():
    """
    Test user signup endpoint.
    """
    email = random_email()
    response = client.post("/auth/signup", json={"email": email, "password": "password123"})
    assert response.status_code == 200, response.text
    assert response.json()["email"] == email

def test_login():
    """
    Test user login endpoint.
    """
    email = random_email()
    client.post("/auth/signup", json={"email": email, "password": "password123"})
    response = client.post("/auth/login", data={"username": email, "password": "password123"})
    assert response.status_code == 200, response.text
    assert "access_token" in response.json()
    token = response.json()["access_token"]
    assert token is not None
    return token

def test_add_post():
    """
    Test adding a new post endpoint.
    """
    token = test_login()
    response = client.post("/posts/addpost", json={"text": "This is a test post"}, headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200, response.text
    assert response.json()["text"] == "This is a test post"

def test_get_posts():
    """
    Test getting all posts for the current user.
    """
    token = test_login()
    response = client.get("/posts", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200, response.text
    assert isinstance(response.json(), list)

def test_delete_post():
    """
    Test deleting a post endpoint.
    """
    token = test_login()
    get_posts_response = client.get("/posts", headers={"Authorization": f"Bearer {token}"})
    posts = get_posts_response.json()
    if posts:
        post_id = posts[0]["id"]
        delete_response = client.delete(f"/posts/deletepost/{post_id}", headers={"Authorization": f"Bearer {token}"})
        assert delete_response.status_code == 200, delete_response.text
        assert delete_response.json() == {"detail": "Post deleted"}
    else:
        print("No posts to delete.")
