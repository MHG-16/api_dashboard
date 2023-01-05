# -*- coding: utf-8 -*-
from contextlib import suppress
from flask.cli import FlaskGroup

from app.run import app
from app.user.models import Users
from app.utils.database import engine, SESSION

cli = FlaskGroup(app)


def init_db():
    with suppress(Exception):
        Users.__table__.drop(engine)
    Users.__table__.create(engine)


@cli.command("create_db")
def create_db():
    init_db()
    SESSION.commit()


if __name__ == "__main__":
    app.config["debug"] = True
    app.run()
    cli()
