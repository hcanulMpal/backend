from ..models import db, Imagen
from ..functions import dbImgCat
from .upFileController import upFile

base = db.session
U = upFile()

class ImageCtl:

    def saveImage(self, url, data):
        print(data)
        print("Llega aqui")
        imagen = Imagen(
            url_photo = url,
            imgCategory_id = dbImgCat().findImageCategory(data[0]),
            description = data[1]
        )
        base.add(imagen)
        base.commit()
    