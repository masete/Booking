from flask import Blueprint, request, jsonify
from flask_jwt_extended import (jwt_required, get_jwt_identity, create_access_token)
from datetime import timedelta
from api.models.user_model import Users

user = Users()

user_blueprint = Blueprint("User", __name__)


@user_blueprint.route('/api/v1/add_user', methods=['POST'], strict_slashes=False)
def add_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')

    new_user = user.add_new_user(username, email)
    if new_user:
        return jsonify({"message": "user added successfully"})
    return jsonify({"message": "user not added"})


@user_blueprint.route('/api/auth/login', methods=['POST'], strict_slashes=False)
def user_login():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')

    check_user = user.get_user_by_email(email)

    if not check_user:
        return jsonify({"message": "first signup please"})
    check_username = check_user['username'], username

    if check_username:
        my_identity = dict(
            user_id=check_user.get('user_id'),
            as_admin=check_user.get('as_admin')
        )
        return jsonify({"message": "logged in successfully", "access_token": create_access_token(identity=my_identity,
                                                                                                 expires_delta=timedelta(hours=3))})
    return jsonify({"message": "your email is not recogonised"})


@user_blueprint.route('/api/v1/get_all_users', methods=['GET'], strict_slashes=False)
@jwt_required
def get_all_users():

    user_role = get_jwt_identity()

    if user_role['as_admin'] == False:
        return jsonify({"message": "your not authorised"}), 401

    all_users = user.get_all_users()
    return jsonify({"message": all_users})
