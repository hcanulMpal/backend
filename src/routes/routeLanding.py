from flask import Blueprint, current_app, request, Flask, render_template
from flask_cors import CORS
from ..controllers import OfficialsCtl, GoverningsCtl
from ..controllers.noticesControllers import NoticesCtl
#from ..controllers.AuthorController import AuthorCtl
from ..controllers.CategoryController import CategoryCtl
from ..controllers.blobController import BlobCtl
from ..controllers.upFileController import upFile
from ..controllers import ImageCtl
from ..controllers import NumeroCtl


landing = Blueprint('admini', __name__)
cors = CORS(landing, resources={ r"/api/*":{"origins":"*"}})

Img = ImageCtl()
Offi = OfficialsCtl()
Gobs = GoverningsCtl()
Gover = GoverningsCtl()
#Au = AuthorCtl()
Ca = CategoryCtl()
Noti = NoticesCtl()
Blobe = BlobCtl()
Uf = upFile()
Nc = NumeroCtl()


@landing.route("/api/landing/funcionarios", methods=['GET'])
def setOfficials():
    return Offi.setOfficials() 


@landing.route("/api/landign/regidores", methods=['GET'])
def setGobernings():
    return Gobs.setGoverning()


@landing.route("/api/landing/notices", methods=["GET"])
def setNotices():
    return Noti.setNotices()

#@landing.route("/api/landing/author", methods=["GET"])

#def setAuthor():
 #   return Au.setAuthor()
    
@landing.route("/api/landing/category", methods=["GET"])
def setCategory():
    return Ca.setCategory()

@landing.route("/api/landing/blob/image", methods=["POST"])
def setBlob():
    return Blobe.setBlob(request.file['file'])   
    
@landing.route("/api/upload", methods=['POST'])
def upFile():
    return Uf.uploadFile(request.files['file'])


@landing.route("/api/guardI", methods=['POST'])
def saveI():
    return Img.saveImage(request.json)

    
@landing.route("/api/landing/NumeroE", methods=["GET"])
def setNumero():
    return Nc.setNumero()
