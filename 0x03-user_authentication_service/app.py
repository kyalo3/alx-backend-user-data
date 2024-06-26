#!/usr/bin/env python3
"""
create a simple flask app
"""
from flask import Flask, jsonify, request, abort, redirect
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


@app.route('/users', methods=['POST'], strict_slashes=False)
def status() -> str:
    """
    Return:
        - json payload
    """
    try:
        email = request.form.get("email")
        password = request.form.get("password")
        user = AUTH.register_user(email, password)
        if user:
            return jsonify({"email": f"{email}", "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"})


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login() -> str:
    """ method to login a user"""
    email = request.form.get("email")
    password = request.form.get("password")

    if AUTH.valid_login(email, password) is False:
        abort(401)
    else:
        session_id = AUTH.create_session(email)
        if session_id:
            response = jsonify({"email": email, "message": "logged in"})
            response.set_cookie('session_id', session_id)
            return response


@app.route("/sessions", methods=["DELETE"], strict_slashes=False)
def logout() -> str:
    """ logout a user"""
    try:
        session_id = request.cookie.get("session_id")
        user = AUTH.get_user_from_session(session_id)
        if user:
            AUTH.destroy_session(user.id)
            return redirect("/")
    except NoResultFound:
        abort(403)


@app.route("/profile", methods=["GET"], strict_slashes=False)
def get_profile() -> str:
    """ return the user based on session id"""
    try:
        session_id = request.cookies.get("session_id")
        user = AUTH.get_user_from_session_id(session_id)
        if user:
            return jsonify({"email": user.email}), 200
        abort(403)
    except NoResultFound:
        return None


@app.route("/reset_password", methods=["PUT"], strict_slashes=False)
def update_password() -> str:
    """ function to update the password"""
    try:
        email = request.form.get('email')
        reset_token = request.form.get('reset_token')
        new_password = request.form.get('new_password')

        user = AUTH.find_user_by(email=email)
        if user:
            if user.reset_token == reset_token:
                AUTH.update_password(reset_token, new_password)
                return jsonify(
                    {"email": user.email, "message": "Password updated"})
    except ValueError:
        return None
    except NoResultFound:
        return None


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
