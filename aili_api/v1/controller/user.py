from . import user_router
from aili_api.v1.service.user_service import *
from flask import jsonify


@user_router.route("/")
def index():
    return "index"


@user_router.route("/find")
def index1():
    user = get_user_by_id(1)
    return jsonify(id=str("a"))