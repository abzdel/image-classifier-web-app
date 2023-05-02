from locust import HttpUser, between, task

class WebsiteUser(HttpUser):
    wait_time = between(5, 9)

    @task
    def predict(self):
        self.client.post("/predict", files={"image": open("tiger.jpg", "rb")})
