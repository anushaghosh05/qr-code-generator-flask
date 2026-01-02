from flask import Flask, render_template, request
import qrcode
import os
import uuid

app = Flask(__name__)

# Folder to save QR codes
QR_FOLDER = "static/qrcodes"
os.makedirs(QR_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    qr_path = None

    if request.method == "POST":
        url = request.form["url"]

        # Unique filename
        filename = f"{uuid.uuid4()}.png"
        qr_path = os.path.join(QR_FOLDER, filename)

        # Generate QR
        qr = qrcode.make(url)
        qr.save(qr_path)

    return render_template("index.html", qr_path=qr_path)

if __name__ == "__main__":
    app.run(debug=True)
