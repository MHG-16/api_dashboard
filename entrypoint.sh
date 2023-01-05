#!/bin/bash
exec gunicorn -b 0.0.0.0:8761 -w 4 --threads 4 -t 120 wsgi:app
