from pyzbar import pyzbar
import cv2
import requests
import boto3

# Initialize S3 client
s3 = boto3.client('s3')

# Bucket and object key
bucket_name = 'your_bucket_name'
object_key = 'path/to/pdf-test.png'

# Load the image from S3
response = s3.get_object(Bucket=bucket_name, Key=object_key)
image_bytes = response['Body'].read()
image_np_array = np.frombuffer(image_bytes, np.uint8)
image = cv2.imdecode(image_np_array, cv2.IMREAD_COLOR)

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
