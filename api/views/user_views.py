from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import (jwt_required, get_jwt_identity, create_access_token)
from datetime import timedelta
from api.models.user_model import Users

user = Users()

user_blueprint = Blueprint("User", __name__)


@user_blueprint.route('/api/auth/add_user', methods=['POST'], strict_slashes=False)
def add_user():
    try:
        data = request.get_json(force=True)

        print(data)

        username = data['username']
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']
        password = data['password']

    except KeyError:
        return (
            jsonify(
                {
                    "error": "Please provide the correct keys for the data",
                    "status": 422,
                }
            ),
            422,
        )

    user_exists = user.get_user_by_email(email)

    # new_user = user.add_new_user(username, first_name, last_name, email, password)

    if user_exists:
        return jsonify({"status": "failure", "error": {"message": "User already exists"}}), 400
    else:
        user.add_new_user(username, first_name, last_name, email, password)
    response = make_response((jsonify({"status": "success", "message": "user added successfully"}), 201))
    return response


@user_blueprint.route('/api/auth/login', methods=['POST'], strict_slashes=False)
def user_login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    check_user = user.get_user_by_email(email)

    if not check_user:
        return jsonify({"message": "first signup please"})
    check_pwd = check_user['password']==password

    if check_pwd:
        my_identity = dict(
            user_id=check_user.get('user_id'),
            as_admin=check_user.get('as_admin')
        )
        return jsonify({"message": "logged in successfully", "access_token": create_access_token(identity=my_identity,
                                                                                                 expires_delta=timedelta(hours=3))})
    return jsonify({"message": "your email or password is incorrect"})


@user_blueprint.route('/api/v1/get_all_users', methods=['GET'], strict_slashes=False)
@jwt_required
def get_all_users():

    user_role = get_jwt_identity()

    if user_role['as_admin'] == False:
        return jsonify({"message": "your not authorised"}), 401

    all_users = user.get_all_users()
    return jsonify({"message": all_users})
