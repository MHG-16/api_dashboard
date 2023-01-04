# -*- coding: utf-8 -*-
from flask import jsonify

from app.user.models import Users
from app.utils.database import SESSION
from app.utils.gen_utils import hash_with_bcrypt


def insert(data: dict) -> dict:
    # pylint: disable=W0703
    try:
        data["genre"] = 0 if data.get("genre") == "m" else 1
        user = Users(**data)
        user.password = hash_with_bcrypt(user.password)
        SESSION.add(user)
        SESSION.commit()
    except Exception as err:
        return jsonify({"error": True, "message": str(err)}), 406
    return (jsonify({"error": False, "message": "user is created successfully"}), 200)


def verify_existance_mail(mail: str) -> bool:
    user = SESSION.query(Users).filter(Users.email == mail).first()
    return user is not None
