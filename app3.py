import boto3
from flask import Flask, jsonify, render_template, request
import base64
import os
import json, requests
import io
from PIL import Image


app = Flask(__name__)


session = boto3.Session(region_name='us-east-1')
sagemaker_client = boto3.client('sagemaker-runtime')

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':

        print("Classifying image...")
        image_file = request.files['image']

        # Set up the endpoint name and the input data
        endpoint_name = "huggingface-pytorch-inference-2023-05-02-00-15-37-215"

        # Convert the image to bytes
        with io.BytesIO(image_file) as buffer:
            image = Image.open(buffer)
            image.save(buffer, format='JPEG')
            image_bytes = buffer.getvalue()

        # Send the request to the endpoint
        response = sagemaker_client.invoke_endpoint(
            EndpointName=endpoint_name,
            ContentType='image/jpeg',
            Body=image_bytes
        )

        # Get the response
        result = response['Body'].read().decode('utf-8')

        return result

    # render the home template for GET requests
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
