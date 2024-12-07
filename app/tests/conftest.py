import pytest
from app import app, db

@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"  # In-memory DB for tests
    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.drop_all()
