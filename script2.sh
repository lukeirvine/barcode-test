#! /bin/bash

conda create -p ./venv-python3.12 python=3.12 -y
conda activate ./venv-python3.12
pip3 install --target=./venv-python3.12/lib/python3.12 requests
pip3 install --target=./venv-python3.12/lib/python3.12 opencv-python
conda install -p ./venv-python3.12 conda-forge::pyzbar
bash copy-binaries.sh