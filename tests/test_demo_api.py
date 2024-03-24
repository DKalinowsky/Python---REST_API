def test_signUp(client):
    response = client.post('/sign_up', data={
        "email": "test@test.pl",
        "firstName": "Testing",
        "password1": "password1",
        "password2": "password1",
    }, follow_redirects=True)

    assert response.status_code == 200

def test_login(client):
    response = client.post('/login', data={
        "email":"test@test.pl",
        "password":"password1"
    }, follow_redirects=True)

    assert response.status_code == 200

def test_auth_unknown_user(client):
    response = client.post('/login', data={
        "email": "",
        "password": ""
    })

    assert b'Email does not exist.' in response.data

def test_create_notes(client):
    response = client.post('/login', data={
        "email":"test@test.pl",
        "password":"password1"
    }, follow_redirects=True)

    assert response.status_code == 200
    
    response = client.post('/notes', data={
        "note": "some random text"
    })

    assert b'some random text' in response.data