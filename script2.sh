#! /bin/bash

conda create -p ./venv-python3.12 python=3.12 -y
conda activate ./venv-python3.12
sudo yum install mesa-libGL
pip3 install --target=./python requests
pip3 install --target=./python opencv-python
conda install -p ./python conda-forge::pyzbar
bash copy-binaries.sh
# show path dependencies for opencv-python to make sure none are coming from /lib64
ldd ./python/cv2/cv2.abi3.so