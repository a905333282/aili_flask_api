from . import user_router
from aili_api.v1.service.user_service import *
from flask import jsonify
from flask import request

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import current_user
from flask_jwt_extended import get_jwt

@user_router.route("/")
def index():
    return "index"


@user_router.route("/find")
def index1():
    user = get_user_by_id(1)
    return jsonify(id=str("a"))


# Create a route to authenticate your users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.
@user_router.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    user = User.query.filter_by(username=username).one_or_none()
    if not user or not user.check_password(password):
        return jsonify("Wrong username or password"), 401

    # Notice that we are passing in the actual sqlalchemy user object here
    additional_claims = {"aud": "some_audience", "foo": "bar"}
    access_token = create_access_token(identity=user, additional_claims=additional_claims)
    return jsonify(access_token=access_token)


@user_router.route("/who_am_i", methods=["GET"])
@jwt_required()
def protected():
    # We can now access our sqlalchemy User object via `current_user`.
    return jsonify(
        id=current_user.id,
        full_name=current_user.full_name,
        username=current_user.username,
    )


@user_router.route("/protected", methods=["GET"])
@jwt_required()
def protecte():
    claims = get_jwt()
    return jsonify(foo=claims["foo"])