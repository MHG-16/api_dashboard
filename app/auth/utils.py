# -*- coding: utf-8 -*-
import secrets
from flask import jsonify

from app.user.models import Users
from app.utils.auth_utils import check_login_by_email
from app.utils.db_utils import updatequery
from app.utils.database import SESSION


def verify_email_and_password(email: str, password: str) -> dict:
    login = check_login_by_email(email, password)
    if login == -1:
        return jsonify({"error": True, "message": "Unkown email"}), 400
    if login == 1:
        return update_token_get_id_user(email)
    return jsonify({"error": True, "message": "Password is incorrect"}), 400


def update_token_by_email(email: str):
    token = secrets.token_hex()
    query = f"UPDATE users SET access_token = '{token}' where email = '{email}'"
    return token if updatequery(query) else None


def update_token_get_id_user(email: str) -> dict:
    if res := update_token_by_email(email):
        return (
            jsonify(
                {
                    "error": False,
                    "message": {
                        "access_token": res,
                        "id_user": SESSION.query(Users)
                        .filter(Users.email == email)
                        .first()
                        .id_user,
                    },
                }
            ),
            200,
        )
    return (
        jsonify({"error": True, "message": "Server error(Access Token update)"}),
        405,
    )


def update_token_by_access_token(access_token: str):
    token = secrets.token_hex()
    query = f"UPDATE users SET access_token = '{token}' where access_token = '{access_token}'"
    return bool(updatequery(query))
