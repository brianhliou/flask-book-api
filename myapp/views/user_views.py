
from flask import Flask, Blueprint, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from ..models.user import User

users = []
user_blueprint = Blueprint('user_blueprint', __name__)

@user_blueprint.route('/register', methods=['POST'])
def register():
    new_user = request.get_json()
    username = new_user.get('username')
    password = new_user.get('password')

    if username and password:
        hashed_password = generate_password_hash(password, method='scrypt')
        id = len(users) + 1
        new_user_obj = User(id, username, hashed_password)
        users.append(vars(new_user_obj))
        return jsonify({'id': id, 'username': username}), 201
    else:
        return jsonify({'error': 'Username or Password is missing'}), 400

@user_blueprint.route('/login', methods=['POST'])
def login():
    credentials = request.get_json()
    username = credentials.get('username')
    password = credentials.get('password')

    if username and password:
        user = next((user for user in users if user["username"] == username), None)
        if user and check_password_hash(user['password'], password):
            return jsonify({'id': user['id'], 'username': user['username']}), 200
        else:
            return jsonify({'error': 'Invalid username or password'}), 401
    else:
        return jsonify({'error': 'Username or Password is missing'}), 400