#!/bin/bash

set -e

# Install system packages
sudo apt-get update
sudo apt-get install -y python3 python3-pip

# Install Python packages
pip3 install --upgrade pip
pip3 install -r requirements.txt

exit 0
