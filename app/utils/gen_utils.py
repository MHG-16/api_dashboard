# -*- coding: utf-8 -*-
from datetime import datetime
import hashlib
from uuid import uuid4
import bcrypt


def hash_with_bcrypt(var: str) -> str:
    if var:
        byte_var = var.encode("utf-8")
        my_salt = bcrypt.gensalt()
        return bcrypt.hashpw(byte_var, my_salt)
    return var


def hash_with_md5(var):
    return hashlib.md5(str(var).encode("utf-8")).hexdigest() if var else var


def validate_format_date(date: str, format_date: str):
    try:
        datetime.strptime(date, format_date)
    except ValueError as err:
        raise ValueError(f"{date} is not a valid date") from err
    return date


def get_unique_id() -> str:
    return uuid4().hex
