from .config_vars import *
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    RBAC_USE_WHITE = True
    PYTHON_VER_MIN_REQUIRED = "3.8.0"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    ALLOWED_EXTENSIONS = set(["xls", "xlsx", "dat"])


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True
    SECRET_KEY = DEV_SECRET_KEY
    SQLALCHEMY_DATABASE_URI = f"mysql://{DEV_DB_USER}:{DEV_DB_PASS}@{DEV_DB_HOST}/{DEV_DB_NAME}"
    STATIC_FOLDER_DOC = basedir + "/static/pdfs/"


class ProductionConfig(Config):
    SECRET_KEY = SECRET_KEY
    SQLALCHEMY_DATABASE_URI = f"mysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
    STATIC_FOLDER_DOC = basedir + "/static/pdfs/"
    

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
}