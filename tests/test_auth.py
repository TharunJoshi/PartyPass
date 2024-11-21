         # Tests for auth routes
def test_signup(client):
    response = client.post('/auth/signup', json={
        "email": "test@example.com",
        "password": "password123"
    })
    assert response.status_code == 201
    assert response.json['message'] == "User registered successfully"

def test_login(client):
    client.post('/auth/signup', json={
        "email": "test@example.com",
        "password": "password123"
    })
    response = client.post('/auth/login', json={
        "email": "test@example.com",
        "password": "password123"
    })
    assert response.status_code == 200
    assert "token" in response.json
