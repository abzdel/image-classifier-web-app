import base64

from app import app

def test_home_page():
    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200


def test_predict_page():
    with app.test_client() as client:
        # upload tiger.jpg as test image
        with open("tiger.jpg", "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode("utf-8")
        
        response = client.post(
            "/",
            content_type="multipart/form-data",
            data={
                "image": ("tiger.jpg", encoded_image),
            },
        )

        assert response.status_code == 200


def test_invalid_request():
    with app.test_client() as client:
        response = client.post("/")
        assert response.status_code == 400
        assert b"Bad Request" in response.data
