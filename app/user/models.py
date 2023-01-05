# -*- coding: utf-8 -*-
# pylint: disable=R0903
from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, Date, Boolean

from ..utils.database import Base, SESSION


class Users(Base):
    # pylint: disable=R0902
    __tablename__ = "users"

    id_user = Column(Integer, primary_key=True)
    last_name = Column(String(25), nullable=False)
    first_name = Column(String(25), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    tel = Column(String(25), nullable=False)
    user_status = Column(Integer, nullable=False)
    genre = Column(Boolean, nullable=False)
    access_token = Column(String(255), nullable=True)

    def __init__(
        self,
        id_user=None,
        last_name=None,
        first_name=None,
        email=None,
        password=None,
        date_of_birth=None,
        tel=None,
        user_status=None,
        genre=None,
    ):
        # pylint: disable=R0913
        self.id_user = id_user
        self.last_name = last_name
        self.first_name = first_name
        self.email = email
        self.password = password
        self.date_of_birth = date_of_birth
        self.tel = tel
        self.user_status = user_status
        self.genre = genre


@dataclass
class UserActions:
    adresse_email: str
    password: str

    def get(self):
        data = SESSION.query(Users).filter(Users.email.like(self.adresse_email))
        return Users.dump(data)

    def update_password(self):
        return (
            SESSION.query(Users)
            .filter(Users.email.like(self.adresse_email))
            .update({"password": self.password})
        )
