import base64
import json
import boto3
import os

with open("tiger.jpg", "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode("utf-8")

# Create a test event
event = {"image": encoded_image}

# Invoke the lambda function
client = boto3.client("lambda")
response = client.invoke(
    FunctionName=os.environ['LAMBDA_NAME'],
    Payload=json.dumps(event)
)

# Print the response from the lambda function
print(response["Payload"].read().decode("utf-8"))
