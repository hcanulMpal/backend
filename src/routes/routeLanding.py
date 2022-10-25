from flask import Blueprint, current_app, request
from flask_cors import CORS
from ..controllers import OfficialsCtl, GoverningsCtl


landing = Blueprint('admini', __name__)
cors = CORS(landing, resources={ r"/api/*":{"origins":"*"}})


Offi = OfficialsCtl()
Gobs = GoverningsCtl()

@landing.route("/api/landign/funcionarios", methods=['GET'])
def setOfficials():
    return Offi.setOfficials() 


@landing.route("/api/landign/regidores", methods=['GET'])
def setGobernings():
    return Gobs.setGoverning()



