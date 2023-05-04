from flask import Flask, request, render_template
import torch
from PIL import Image
from transformers import AutoFeatureExtractor, ResNetForImageClassification

app = Flask(__name__)

# Load the pre-trained model from Hugging Face
model_name = "microsoft/resnet-18"  # Replace with the name of your pre-trained model
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForSequenceClassification.from_pretrained(model_name)

feature_extractor = AutoFeatureExtractor.from_pretrained("microsoft/resnet-18")
model = ResNetForImageClassification.from_pretrained("microsoft/resnet-18")

model.eval()


# Define a Flask API route to accept images
@app.route("/predict", methods=["POST"])
def predict():
    print("Received request for prediction")

    # show the image that the user has sent
    print(request.files["image"])

    # Get the image from the request
    image_file = request.files["image"]
    image = Image.open(image_file)

    image = image.resize((224, 224))
    inputs = feature_extractor(image, return_tensors="pt")

    with torch.no_grad():
        logits = model(**inputs).logits

    # model predicts one of the 1000 ImageNet classes
    predicted_label = logits.argmax(-1).item()
    print(f"Predicted class: {model.config.id2label[predicted_label]}")

    # Return the prediction to the user
    # return jsonify({'prediction': model.config.id2label[predicted_label]})
    return model.config.id2label[predicted_label]


# Define a Flask API route to serve the HTML file
@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
