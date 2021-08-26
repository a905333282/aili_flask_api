from flask import Flask, jsonify
from utils.GetConfig import Conf
from controller.users import users_router
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

app = Flask(__name__)



# 加载配置
conf = Conf().get_config()
print(conf)
for key in conf:
    print(key)
    print(conf[key])
    app.config[key] = conf[key]
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


# 注册蓝图
app.register_blueprint(users_router, url_prefix='/users')
# 初始化数据库
db = SQLAlchemy(app)
# 初始化jwt
jwt = JWTManager(app)

db.create_all()


app.run(host="0.0.0.0", port=5004, debug=True)



