from flask import Blueprint, current_app, request
from flask_cors import CORS
from ..controllers import OfficialsCtl, GoverningsCtl
from ..controllers.noticesControllers import NoticesCtl


landing = Blueprint('admini', __name__)
cors = CORS(landing, resources={ r"/api/*":{"origins":"*"}})


Offi = OfficialsCtl()
<<<<<<< HEAD
Gobs = GoverningsCtl()
=======
Gover = GoverningsCtl()
Not = NoticesCtl()
>>>>>>> main

@landing.route("/api/landing/funcionarios", methods=['GET'])
def setOfficials():
    return Offi.setOfficials() 


@landing.route("/api/landign/regidores", methods=['GET'])
def setGobernings():
    return Gobs.setGoverning()



<<<<<<< HEAD
=======
@landing.route("/api/landing/regidores", methods=["GET"])
def setGovernings():
    return Gover.setGovernings()


@landing.route("/api/landing/notices", methods=["GET"])
def setNotices():
    return Not.setNotices()
>>>>>>> main
