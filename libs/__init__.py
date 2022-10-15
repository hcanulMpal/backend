from flask import Flask
from .config import config
import pymysql
# from models import db



pymysql.install_as_MySQLdb()



def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    # db.init_app(app)
    # app.app_context().push()
    # db.init_app(app)
    # with app.app_context():
    #     db.create_all()


    return app