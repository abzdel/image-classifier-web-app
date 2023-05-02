import base64
import json
import boto3

with open("tiger.jpg", "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode("utf-8")

# Create a test event
event = {"body": encoded_image}

# Invoke the lambda function
client = boto3.client("lambda")
response = client.invoke(FunctionName="classify", Payload=json.dumps(event))

response_dict = json.loads(response["Payload"].read().decode("utf-8"))
print(json.loads(response_dict.get("body")))
