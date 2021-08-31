# from flask_sqlalchemy import SQLAlchemy
from .dbinit import db
from .jwtinit import jwt
from aili_api.v1.model.user import User


@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return User.query.filter_by(id=identity).one_or_none()