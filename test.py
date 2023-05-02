import base64
import json
import boto3
import os
import requests

with open("tiger.jpg", "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode("utf-8")

# Create a test event
event = {"body": encoded_image}

# Invoke the lambda function
client = boto3.client("lambda")
response = client.invoke(
    FunctionName="classify",
    Payload=json.dumps(event)
)

# response = requests.post(
#     "https://bpmy4zne6hobe2ic7rezjixlb40ercvc.lambda-url.us-east-1.on.aws/",
#     json=event
# )

# Print the response from the lambda function
print(response["Payload"].read().decode("utf-8"))
