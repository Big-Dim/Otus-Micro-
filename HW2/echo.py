mport json
from flask import Flask, request, jsonify, abort

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"status":"success"})

@app.route("/health", methods=["GET"])
def getName():
    return jsonify({"status": "OK"})

app.run(host='0.0.0.0', port=5000)