import base64

# Read the image file in binary mode
with open('tiger.jpg', 'rb') as f:
    image_data = f.read()

# Encode the image data as base64
base64_data = base64.b64encode(image_data).decode('utf-8')


# save to txt file
with open('tiger.txt', 'w') as f:
    f.write(base64_data)
