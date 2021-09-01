from . import user_router
from aili_api.v1.service.user_service import *
from flask import jsonify
from flask import request
from config import ACCESS_EXPIRES
from utils import redis, admin_required
from flask_jwt_extended import create_access_token
from flask_jwt_extended import create_refresh_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import current_user
from flask_jwt_extended import get_jwt


@user_router.route("/test_api")
def index():
    return "api seem ok!"


@user_router.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    user = User.query.filter_by(username=username).one_or_none()
    # 密码验证，身份查询
    if not user or not user.check_password(password):
        return jsonify("Wrong username or password"), 401

    # Notice that we are passing in the actual sqlalchemy user object here
    additional_claims = {"aud": "some_audience", "foo": "bar"}

    access_token = create_access_token(identity=user, additional_claims=additional_claims, fresh=True)
    refresh_token = create_refresh_token(identity=user, additional_claims=additional_claims)
    return jsonify(access_token=access_token, refresh_token=refresh_token)


@user_router.route("/who_am_i", methods=["GET"])
@jwt_required()
def protected():
    # We can now access our sqlalchemy User object via `current_user`.
    identity = get_jwt_identity()
    print(identity)
    return jsonify(
        id=current_user.id,
        full_name=current_user.full_name,
        username=current_user.username,
    )


@user_router.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():

    identity = get_jwt_identity()
    user = get_user_by_id(identity)
    access_token = create_access_token(identity=user, fresh=False)
    return jsonify(access_token=access_token)


@user_router.route("/protected", methods=["GET"])
@admin_required()
def protecte():
    return jsonify(foo="foo")


@user_router.route("/logout", methods=["DELETE"])
@jwt_required()
def logout():
    jti = get_jwt()["jti"]
    redis.set(jti, "", ex=ACCESS_EXPIRES)
    return jsonify(msg="Access token revoked")