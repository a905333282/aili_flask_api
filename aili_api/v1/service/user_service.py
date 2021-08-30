from aili_api.v1.model.user import User


def get_user_by_id(id):
    user = User.query.filter_by(id=id).one_or_none()
    print(user)