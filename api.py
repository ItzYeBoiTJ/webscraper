# api.py
from flask import Flask, jsonify, request
from db import get_all_vulnerabilities, get_vulnerabilities_by_oem

app = Flask(__name__)

@app.route("/vulnerabilities", methods=["GET"])
def all_vulnerabilities():
    """Fetch all vulnerabilities"""
    return jsonify(get_all_vulnerabilities())

@app.route("/vulnerabilities/<string:oem>", methods=["GET"])
def vulnerabilities_by_oem(oem):
    """Fetch vulnerabilities for a specific OEM"""
    return jsonify(get_vulnerabilities_by_oem(oem))

if __name__ == "__main__":
    app.run(debug=True)
