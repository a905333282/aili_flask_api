

class Config(object):
    SECRET_KEY = "super-secret"
    JWT_SECRET_KEY = "super-secret"  # Change this!
    SQLALCHEMY_DATABASE_URI = "mysql://baixiao:123456@39.106.6.245/ali_report?charset=utf8mb4"
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevConfig(Config):
    DEBUG = True

    pass


class ProdConfig(Config):
    pass


config_mapper = {
    "dev": DevConfig,
    "prod": ProdConfig
}