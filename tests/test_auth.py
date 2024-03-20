
import requests

'''def test_signUp(client, app):
    response = client.post('/sing_up')
    email = 'test@test.pl'
    first_name = 'Testing'
    password1 = 'password1'
    password2 = 'password1'
    
    with app.app_context():
        assert User.query.count() == 2
        assert User.query.filter_by().email == "test@test.pl"


def test_auth(app_with_data):
    # when
    response = app_with_data.post(
        url_for("auth.login"),
        json={
            "email": "admin@admin.pl",
            "password": "admin12"
        }
    )
    data = response.json

    # then
    assert response.status_code == 200
    assert "token" in data
def test_auth_unknown_user(app_with_data):
    # when
    response = app_with_data.post(
        url_for("auth.login"),
        json={
            "email": "",
            "password": ""
        }
    )

    # then
    assert response.status_code == 404

def test_auth_failed_login(app_with_data):
    # when
    response = app_with_data.post(
        url_for("auth.login"),
        json={
            "email": "",
            "password": ""
        }
    )

    # then
    assert response.status_code == 404
class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING']= True
        self.client = app.test_client()
    
    def test_login_user_not_found(self):'''


ENDPOINT = "http://127.0.0.1:5000/"


def test_can_call_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200