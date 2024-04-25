#!/usr/bin/env python3
"""
create a simple flask app
"""
from flask import Flask, jsonify, request, abort
from sqlalchemy.orm.exc import NoResultFound
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def create_app() -> str:
    """
    Returns:
      - JSON payload

    """
    return jsonify({"message": "Bienvenue"})


@app.route('/', methods=['POST'], strict_slashes=False)
def status():
    """
    Return:
        - json payload
    """
    if user:
        return jsonify({
            "email": "<registered email>",
            "message": "user created"
        })

    else:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
