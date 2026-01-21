from flask import Flask, request, jsonify
from cloud.storage import save_file

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files["file"]
    save_file(file.filename, file.read())
    return jsonify({"message": "File uploaded successfully"})

if __name__ == "__main__":
    app.run(debug=True)
