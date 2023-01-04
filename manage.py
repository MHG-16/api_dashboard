# -*- coding: utf-8 -*-
from flask.cli import FlaskGroup

from app.run import app

cli = FlaskGroup(app)

if __name__ == "__main__":
    app.config["debug"] = True
    cli()
