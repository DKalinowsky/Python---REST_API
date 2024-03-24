def test_home_route(app):
    response = app.test_client().get('/login?next=/')
    assert response.status_code == 200
    assert b'<title>Login</title>' in response.data