import pytest
from website import create_app, db
# from website.models import User
# from sqlalchemy import delete
# from werkzeug.security import generate_password_hash

@pytest.fixture()
def app():
    app=create_app()
    app.config.update({
        "TESTING": True,
    })

    with app.app_context():
        db.create_all()

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
