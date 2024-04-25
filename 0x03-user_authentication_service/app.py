#!/usr/bin/env python3
"""
create a simple flask app
"""
from flask import Flask, jsonify, request. abort
from auth import Auth

app = Flask(__name__)
Auth = Auth()

@app.route('/', methods=[GET], strict_slashes=False)
def create_app() -> str:
    """returns a JSON payload form
    """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
