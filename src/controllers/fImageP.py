from ..models import db, Imagen
from ..functions import dbImgCat
from .upFileController import upFile

base = db.session
U = upFile()

class ImageCtl:

    def saveImage(self, data):
        imagen = Imagen(
            #url_photo = U.uploadFile(data['0']),
            imgCategory_id = dbImgCat().findImageCategory(data['0']),
            description = data['1']
        )
        base.add(imagen)
        base.commit()
    