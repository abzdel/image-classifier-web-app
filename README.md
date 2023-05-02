[![Makefile CI](https://github.com/abzdel/image-classifier-web-app/actions/workflows/makefile.yml/badge.svg)](https://github.com/abzdel/image-classifier-web-app/actions/workflows/makefile.yml)

# Image Classifier Web Service

This is a web application that allows users to upload an image and receive a classification prediction for that image using a pre-trained deep learning model. The application uses Flask as the backend framework, which invokes an AWS Lambda function to make requests to a pre-deployed Amazon SageMaker endpoint for image classification. The predicted labels are then returned to the user and displayed on the web page.

A link to the webpage where you can try this yourself is [here!](https://4awasaff22.us-east-1.awsapprunner.com/)

# Architectural Diagram
![721final drawio](https://user-images.githubusercontent.com/55398496/235781148-05f3272d-d134-463c-b63c-3e085cdad793.png)
