import boto3
from flask import Flask, jsonify, render_template, request
import base64
import os
import json, requests
import io
from PIL import Image


app = Flask(__name__)

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
        client = boto3.client('lambda')
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
    app.run(debug=True)
