from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, current_user


users_router = Blueprint('users_router', __name__)

from models.users import User


@users_router.route('/', methods=["GET"])
def login1():
    return jsonify(access_token="OK")


@users_router.route('/login', methods=["POST"])
def login():
    # print(request.get_data())
    # username = request.json.get("username", None)
    # password = request.json.get("password", None)
    #
    # user = User.query.filter_by(username=username).one_or_none()
    # if not user or not user.check_password(password):
    #     return jsonify("Wrong username or password"), 401
    #
    # # Notice that we are passing in the actual sqlalchemy user object here
    # access_token = create_access_token(identity=user)
    return jsonify(access_token="access_token")


# Protect a route with jwt_required, which will kick out requests
# without a valid JWT present.
@users_router.route("/who_am_i", methods=["GET"])
@jwt_required()
def protected():
    # We can now access our sqlalchemy User object via `current_user`.
    return jsonify(
        id=current_user.id,
        full_name=current_user.full_name,
        username=current_user.username,
    )