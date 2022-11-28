from flask import Flask
from .config import config
import pymysql
from src.models import db
from src.controllers.validate import Valide
from src.middlewares import verifyAndCreateData



def create_app(config_name='development'):
    pymysql.install_as_MySQLdb()
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)
    app.app_context().push()
    db.init_app(app)
    with app.app_context():
        db.create_all()

    Valide().valideTables()
    verifyAndCreateData()
    

    #TODO: importacion para asignar a los Blueprints
    from src.routes import landing, auth, arch

     #TODO: Configuracion de los BluePrints
    app.register_blueprint(landing)
    app.register_blueprint(auth)
    app.register_blueprint(arch)
    
    return app