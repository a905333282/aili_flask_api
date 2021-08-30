from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_mapper
from flask_wtf import CSRFProtect

db = SQLAlchemy()


def create_app(config):
    """
    以工厂模式创建 app 对象
    :param: config: str 配置app模式，可选值"dev", "prod"
    :return:
    """

    app = Flask(__name__)
    app.config.from_object(config_mapper.get(config))

    db.init_app(app)

    CSRFProtect(app)

    from aili_api import v1

    app.register_blueprint(v1.controller.user_router, url_prefix="/api/v1/user")

    return app

