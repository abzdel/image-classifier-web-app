import json
import requests
from PIL import Image
import base64

# load in image with PIL

with open("tiger.jpg", "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode("utf-8")

# Create a test event
event = {"body": encoded_image}


r = requests.post(
    "https://fypjhju186.execute-api.us-east-1.amazonaws.com/PROD/classifier",
    data=event)

print(r.content)