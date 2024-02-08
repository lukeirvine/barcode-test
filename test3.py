from pyzbar import pyzbar
import cv2
import requests

# Load the image
image = cv2.imread('pdf-test.png')

# Decode barcodes in the image
barcodes = pyzbar.decode(image)

# Sort barcodes by barcodeData
barcodes.sort(key=lambda x: x.data.decode('utf-8'))

# List to store barcodeData values
barcode_data_list = []

# Iterate over the sorted barcodes and collect barcodeData values
for barcode in barcodes:
  barcode_data = barcode.data.decode('utf-8')
  barcode_data_list.append(barcode_data)
  print("Barcode: {}".format(barcode_data))

# URL of the server endpoint
url = "https://a3ab-71-94-190-241.ngrok-free.app/ducky-derby-tickets/us-central1/addImageData"

# Data to send to the server
data = {
  "barcodeData": barcode_data_list
}

# Send a POST request to the server
response = requests.post(url, json=data)

# Check the response from the server
if response.status_code == 200:
  print("Data sent successfully!")
else:
  print("Failed to send data. Status code:", response.status_code)
  print("Response:", response.text)
