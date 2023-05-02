import boto3
from flask import Flask, jsonify, render_template, request
import base64
import os
import json, requests

app = Flask(__name__)

# create an API Gateway SDK client
apigateway_client = boto3.client('apigateway')

# create a Lambda SDK client
lambda_client = boto3.client('lambda')

session = boto3.Session(region_name='us-east-1')
#client = session.client('apigatewaymanagementapi', endpoint_url=os.environ['API_PATH'])

# define your API Gateway REST API ID and resource path
#rest_api_id = os.environ['API_GATEWAY_ID']
#resource_path = os.environ['API_PATH']
resource_path = "https://fypjhju186.execute-api.us-east-1.amazonaws.com/PROD/classifier"
rest_api_id = "fypjhju186"

# define your Lambda function name
#lambda_function_name = os.environ['LAMBDA_NAME']
lambda_function_name = "classify"

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':

        print("Classifying image...")
        image_file = request.files['image']

        image_bytes = image_file.read()
        encoded_image = base64.b64encode(image_bytes).decode('utf-8')

        # Send a POST request to the API Gateway endpoint
        #response = requests.post(resource_path + "/classifier", json=encoded_image)

        # invoke lambda function
        # Create a test event
        event = {"body": encoded_image}

        # Invoke the lambda function
        client = boto3.client("lambda")
        response = client.invoke(
            FunctionName="classify",
            Payload=json.dumps(event)
        )
        
        response_dict = json.loads(response["Payload"].read().decode("utf-8"))
        print(json.loads(response_dict.get('body')))

        return json.loads(response_dict.get('body'))

        # Parse the response JSON and return the prediction
        #prediction = json.loads(response.content)
        #return prediction

    # render the home template for GET requests
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
