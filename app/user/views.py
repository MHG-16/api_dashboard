# -*- coding: utf-8 -*-
from flask import request, jsonify
from flask import Blueprint

from app.user.utils import insert, verify_existance_mail


app = Blueprint("Users API", __name__)


@app.route("/create", methods=["POST"])
def create_user():
    data_user = request.json
    mail_user = data_user.get("email")
    if verify_existance_mail(mail_user):
        return (
            jsonify(
                {
                    "error": True,
                    "message": f"Il y a un compte avec cet addresse email:{mail_user}",
                }
            ),
            409,
        )
    return insert(data_user)
