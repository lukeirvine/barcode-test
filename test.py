from pyzbar import pyzbar
import cv2

image = cv2.imread('pdf-test.png')
barcodes = pyzbar.decode(image)
for barcode in barcodes:
    (x, y, w, h) = barcode.rect
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

    barcodeData = barcode.data.decode('utf-8')
    barcodeType = barcode.type
    text = "{} ( {} )".format(barcodeData, barcodeType)
    cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 2)

    print("Information : \n Found Type : {} Barcode : {}".format(barcodeType, barcodeData))
