from flask import Blueprint, current_app, request
from flask_cors import CORS
from ..controllers import OfficialsCtl


landing = Blueprint('admini', __name__)
cors = CORS(landing, resources={ r"/api/*":{"origins":"*"}})


Offi = OfficialsCtl()

@landing.route("/api/landign/regidores", methods=['GET'])
def setOfficials():
    return Offi.setOfficials()