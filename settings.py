
# -*- coding: utf-8 -*-
"""
DEFINE CONFIG IN .env FILE & INITILIZE PARAMETRES HERE :)
SEE TEMPLATE .env.tpl FOR EXAMPLES
"""
import os
from dotenv import load_dotenv

load_dotenv()


# Database configurations variables
DB_HOST = os.environ.get("DB_HOST")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DATABASES = os.environ.get("DATABASE")

# sqlalchemy database url variable
SQLALCHEMY_DATABASE_URL = os.environ.get("SQLALCHEMY_DATABASE_URL")