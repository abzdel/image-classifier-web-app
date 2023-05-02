import boto3
from flask import Flask, jsonify, render_template, request
import base64
import os
import json, requests
import io
from PIL import Image



app = Flask(__name__)

# Get AWS credentials from environment variables
aws_access_key_id = os.environ['AWS_ACCESS']
aws_secret_access_key = os.environ['AWS_SECRET']

# Create a new session using the credentials
session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

client = boto3.client('lambda' , region_name='us-east-1')

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':

        print("Classifying image...")
        # Read the image file from the request
        image_file = request.files['image']
        image_data = image_file.read()
        
        # Encode the image data in base64 format
        encoded_image = base64.b64encode(image_data).decode('utf-8')

        # Create the payload for the Lambda function
        event = {
            'body': encoded_image
        }

        # Invoke the Lambda function
        response = client.invoke(
            FunctionName='classify',
            Payload=json.dumps(event)
        )

        # Parse the response from the Lambda function
        response_dict = json.loads(response['Payload'].read().decode('utf-8'))
        #predictions = response_dict.get('predictions')
        predictions = json.loads(response_dict.get('body'))

        

        #return json.loads(response_dict.get('body'))
        return render_template('preds.html', results=predictions)
        #return render_template('preds.html', results=response_dict.get('body'))


    # render the home template for GET requests
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=8080, debug=True)
