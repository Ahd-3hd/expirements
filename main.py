from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route("/mymodel")
def hello_world():
    return send_from_directory('.', './MobileNetV2.mlmodel', as_attachment=True)

