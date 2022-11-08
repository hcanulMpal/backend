from flask import Flask
from .config import config
import pymysql
from src.models import db
from src.controllers.validate import Valide



def create_app(config_name='production'):
    pymysql.install_as_MySQLdb()
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)
    app.app_context().push()
    db.init_app(app)
    with app.app_context():
        db.create_all()

    Valide().valideTables()

    #TODO: importacion para asignar a los Blueprints
    from src.routes import landing

     #TODO: Configuracion de los BluePrints
    app.register_blueprint(landing)
    
    return app