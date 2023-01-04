# -*- coding: utf-8 -*-
import bcrypt

from app.user.models import Users
from app.user.utils import verify_existance_mail
from app.utils.database import SESSION


def check_login_by_email(email: str, password: str):
    if verify_existance_mail(email) is False:
        return -1
    return bool(verify_password(email, password))


def verify_password(email: str, password: str) -> bool:
    user = SESSION.query(Users).filter(Users.email == email).first()
    return bcrypt.checkpw(password.encode(), user.password.encode())
