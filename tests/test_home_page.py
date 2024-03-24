def test_home_route_get(client):
    response = client.get('/login?next=/')
    assert response.status_code == 200
    assert b'<title>Login</title>' in response.data

def test_home_route_post(client):
    response = client.post('/login?next=/')
    assert response.status_code == 200
    assert b'<title>Login</title>' in response.data