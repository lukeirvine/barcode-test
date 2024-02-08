from pyzbar import pyzbar
import cv2

image = cv2.imread('pdf-test.png')
barcodes = pyzbar.decode(image)

# sort barcodes by barcodeData
barcodes.sort(key=lambda x: x.data.decode('utf-8'))

for barcode in barcodes:
    barcodeData = barcode.data.decode('utf-8')
    barcodeType = barcode.type

    print("Barcode: {} - {}".format(barcodeData, barcodeType))