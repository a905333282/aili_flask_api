from datetime import timedelta

ACCESS_EXPIRES = timedelta(seconds=1)
REFRESH_EXPIRES = timedelta(seconds=1)

class Config(object):
    SECRET_KEY = "super-secret"
    JWT_SECRET_KEY = "super-secret"  # Change this!
    SQLALCHEMY_DATABASE_URI = "mysql://baixiao:123456@39.106.6.245/ali_report?charset=utf8mb4"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    JWT_ACCESS_TOKEN_EXPIRES = ACCESS_EXPIRES
    JWT_REFRESH_TOKEN_EXPIRES = REFRESH_EXPIRES
    REDIS_HOST = "192.168.146.134"
    REDIS_POST = 6379


class DevConfig(Config):
    DEBUG = True

    pass


class ProdConfig(Config):
    pass


config_mapper = {
    "dev": DevConfig,
    "prod": ProdConfig
}