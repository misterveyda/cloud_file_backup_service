from flask import Flask, send_file
from cloud.config import CLOUD_STORAGE_PATH

app = Flask(__name__)

@app.route("/download/<filename>")
def download_file(filename):
    return send_file(CLOUD_STORAGE_PATH + filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
