# Install the Kaggle library
!pip install -q kaggle

# Set Kaggle credentials
import json
import os

# Replace the following with your Kaggle username and API key

kaggle_info = {
    "username": "user_kaggle",
    "key": "api_key"
}

# Save Kaggle credentials to a JSON file
os.makedirs("/root/.kaggle", exist_ok=True)
with open("/root/.kaggle/kaggle.json", "w") as file:
    json.dump(kaggle_info, file)

# Change the permissions of the file
!chmod 600 /root/.kaggle/kaggle.json

# Download the dataset
# Inser the API command to download the dataset, example bellow
#!kaggle datasets download -d likhon148/animal-data 

# Unzip the dataset

#!mkdir /content/gpiosenka/sports-classification
#!unzip -q animal-data.zip -d animal-data

# List the contents of the directory
#!ls /content/animal-data
