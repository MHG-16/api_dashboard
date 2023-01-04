#!/bin/bash
exec gunicorn --config /usr/src/app/gunicorn_config.py wsgi:app
