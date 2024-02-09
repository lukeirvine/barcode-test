# DONT RUN THIS SCRIPT

# terminate script
exit 0

aws s3 cp example.txt s3://barcode-test-002/

du -sh venv-python3.12

zip -r lambda-layer.zip python