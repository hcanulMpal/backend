from flask import Blueprint, current_app, request
from flask_cors import CORS
from ..controllers import OfficialsCtl, GoverningsCtl
from ..controllers.noticesControllers import NoticesCtl
from ..controllers.prensaControllers import PrensaCtl
from ..controllers.AuthorController import AuthorCtl
from ..controllers.CategoryController import CategoryCtl



landing = Blueprint('admini', __name__)
cors = CORS(landing, resources={ r"/api/*":{"origins":"*"}})


Offi = OfficialsCtl()
Gover = GoverningsCtl()
Not = NoticesCtl()
Pre = PrensaCtl
Au = AuthorCtl
Ca = CategoryCtl


@landing.route("/api/landing/funcionarios", methods=['GET'])
def setOfficials():
    return Offi.setOfficials() 


@landing.route("/api/landing/regidores", methods=["GET"])
def setGovernings():
    return Gover.setGovernings()


@landing.route("/api/landing/notices", methods=["GET"])
def setNotices():
    return Not.setNotices()

@landing.route("/api/landing/prensa", methods=["GET"])
def setPrensa():
    return Pre.setPrensa()

@landing.route("/api/landing/author", methods=["GET"])
def setAuthor():
    return Au.setAuthor()
    
@landing.route("/api/landing/category", methods=["GET"])
def setCategory():
    return Ca.setCategory()



