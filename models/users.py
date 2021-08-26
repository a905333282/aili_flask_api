from myapp import db
from hmac import compare_digest

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False)
    password = Column(String(20), nullable=False)
    phone = Column(String(20))
    email = Column(String(100))
    full_name = Column(String(20))

    def check_password(self, password):
        return compare_digest(password, "password")
