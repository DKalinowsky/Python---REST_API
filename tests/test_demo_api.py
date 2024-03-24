from website.models import User

# def test_signUp(app, client):
#     response = client.post('/sing_up', data=dict(
#         email='test55@test',
#         firstName='test55',
#         password1='test5541',
#         password2='test5541'
#     ), follow_redirects=True)
    
#     assert response.status_code == 200
#     # with app.app_context():
#     #     assert User.query.count() == 2
#     #     assert User.query.filter_by().email == "test@test.pl"


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

