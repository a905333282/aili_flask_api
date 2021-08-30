# coding: utf-8

from sqlalchemy import Column, Integer, String
from aili_api import db


class User(db.Model):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False)
    password = Column(String(20), nullable=False)
    phone = Column(String(20))
    email = Column(String(100))
    full_name = Column(String(20))

    def __str__(self):
        return str(self.username)
