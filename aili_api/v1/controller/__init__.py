# coding: utf-8
from flask import Blueprint

user_router = Blueprint("api_v1", __name__)

from . import user