from flask import Blueprint, request, jsonify
from api.models.user_model import Users

user = Users()

user_blueprint = Blueprint("User", __name__)


@user_blueprint.route('/api/v1/add_user', methods=['GET'], strict_slashes=False)
def add_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')

    new_user = user.add_new_user(username, email)
    if new_user:
        return jsonify({"message": "user added successfully"})
    return jsonify({"message": "user nt added"})
