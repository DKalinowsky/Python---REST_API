from website.models import User 

def test_signUp(client, app):
    response = client.post('/sing_up', data={"email" : "test@test.pl", "firstName" : "test", "password1" : "password1", "password2" : "password1"})
    
    with app.app_context():
        assert User.query.first().email == "test@test.pl"

