from flask import Blueprint, current_app, request
from flask_cors import CORS
from ..controllers import OfficialsCtl, GoverningsCtl
from ..controllers.noticesControllers import NoticesCtl
#from ..controllers.prensaControllers import PrensaCtl
from ..controllers.AuthorController import AuthorCtl
from ..controllers.CategoryController import CategoryCtl
from ..controllers.blobController import BlobCtl


landing = Blueprint('admini', __name__)
cors = CORS(landing, resources={ r"/api/*":{"origins":"*"}})


Offi = OfficialsCtl()
Gover = GoverningsCtl()
#Pre = PrensaCtl
Au = AuthorCtl()
Ca = CategoryCtl()
Noti = NoticesCtl()
Blobe = BlobCtl()


@landing.route("/api/landing/funcionarios", methods=['GET'])
def setOfficials():
    return Offi.setOfficials() 


@landing.route("/api/landing/regidores", methods=["GET"])
def setGovernings():
    return Gover.setGovernings()


@landing.route("/api/landing/notices", methods=["GET"])
def setNotices():
    return Noti.setNotices()

@landing.route("/api/landing/prensa", methods=["GET"])
def setPrensa():
    return Pre.setPrensa()

@landing.route("/api/landing/author", methods=["GET"])
def setAuthor():
    return Au.setAuthor()
    
@landing.route("/api/landing/category", methods=["GET"])
def setCategory():
    return Ca.setCategory()

@landing.route("/api/landing/blob/image", methods=["POST"])
def setBlob():
    return Blobe.setBlob(request.file['file'])
    
    
