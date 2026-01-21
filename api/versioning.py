import os
import time
from cloud.storage import save_file

def save_versioned_file(filename, data):
    timestamp = int(time.time())
    versioned_name = f"{timestamp}_{filename}"
    save_file(versioned_name, data)
