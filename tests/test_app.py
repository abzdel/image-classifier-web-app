import pytest
import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to myapp" in response.data


def test_predict_page(client):
    # Upload an image file for testing
    with open("tiger.jpg", "rb") as f:
        data = {"file": (f, "tiger.jpg")}
        response = client.post('/predict', data=data, follow_redirects=True)
        
    assert response.status_code == 200
    assert b"Class" in response.data
    assert b"Confidence" in response.data
