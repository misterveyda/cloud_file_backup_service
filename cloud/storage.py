import os
from cloud.config import CLOUD_STORAGE_PATH

os.makedirs(CLOUD_STORAGE_PATH, exist_ok=True)

def save_file(filename, data):
    with open(CLOUD_STORAGE_PATH + filename, "wb") as f:
        f.write(data)

def get_file(filename):
    path = CLOUD_STORAGE_PATH + filename
    if not os.path.exists(path):
        return None
    with open(path, "rb") as f:
        return f.read()
