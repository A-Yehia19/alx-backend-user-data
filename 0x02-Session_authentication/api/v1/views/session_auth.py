#!/usr/bin/env python3
""" Module of Session Auth Views"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def view_all_users() -> str:
    """ POST /api/v1/auth_session/login """
    user_email = request.form.get('email')
    user_password = request.form.get('password')

    if user_email is None:
        return jsonify({"error": "email missing"}), 400
    
    if user_password is None:
        return jsonify({"error": "password missing"}), 400

    user = User.search({'email': user_email})

    if not user:
        return jsonify({"error": "no user found for this email"}), 404
    
    user = user[0]
    
    if not user.is_valid_password(user_password):
        return jsonify({"error": "wrong password"}), 401
    
    from api.v1.app import auth
    session_id = auth.create_session(user.id)
    cookie_response = getenv('SESSION_NAME')
    user_dict = jsonify(user.to_json())

    user_dict.set_cookie(cookie_response, session_id)
    return user_dict