from flask import Flask, request, jsonify, render_template
import torch
from PIL import Image
import torchvision.transforms as transforms
import numpy as np
from transformers import AutoFeatureExtractor, ResNetForImageClassification
import os

app = Flask(__name__)

# Load the pre-trained model from Hugging Face
model_name = "microsoft/resnet-18" # Replace with the name of your pre-trained model
#tokenizer = AutoTokenizer.from_pretrained(model_name)
#model = AutoModelForSequenceClassification.from_pretrained(model_name)

feature_extractor = AutoFeatureExtractor.from_pretrained("microsoft/resnet-18")
model = ResNetForImageClassification.from_pretrained("microsoft/resnet-18")

model.eval()

# Define a Flask API route to accept images
@app.route('/predict', methods=['POST'])
def predict():
    print('Received request for prediction')
    # Get the image from the request
    image_file = request.files['image']
    image = Image.open(image_file)

    # Process the image to match the input format of the model
    transform = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )
    ])
    image_tensor = transform(image).unsqueeze(0)

    # Make a prediction using the pre-trained model
    with torch.no_grad():
        outputs = model(image_tensor)
        logits = outputs.logits
        probabilities = torch.softmax(logits, dim=1)
        predicted_class = torch.argmax(probabilities, dim=1).item()

    print(f'Predicted class: {predicted_class}')

    # Return the prediction to the user
    return jsonify({'prediction': predicted_class})

# Define a Flask API route to serve the HTML file
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)