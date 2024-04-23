#!/usr/bin/env python3
"""
Route module for the API
"""
from flask import Flask

app = Flask(__name__)


@app.route('/GET')
def create_app() -> str:
    """returns a JSON payload form
    """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
