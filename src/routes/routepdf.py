from flask_cors import CORS
from flask import Blueprint, current_app
from ..reports import Mapa


arch = Blueprint('arch', __name__)
cors = CORS(arch, resources={ r"/api/*":{"origins":"*"}})

ma = Mapa()

@arch.route("/api/arch/mapa", methods =['GET'])
def mapa():
    return ma.mapa()
    
        
