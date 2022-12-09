from ..models import db, Imagen
from .fImageCategory import dbImgCat


base = db.session


class dbImage:

    img = [{
        "url_photo": "https://res.cloudinary.com/municipio-de-felipe-carrillo-puerto/image/upload/v1668618057/u2bqpko0nudbhb8u2qzy.jpg",
        "imgCategory_id":"Carrusel_2",
        "description":"Ta chido",
    }, 
    {
        "url_photo": "https://res.cloudinary.com/municipio-de-felipe-carrillo-puerto/image/upload/v1668630059/n5fow5igwemli1r0faof.jpg",
        "imgCategory_id":"Carrusel_1",
        "description":"Esto es Arte...",
    }]

    def is_Data(self):
        if not Imagen.query.all():
            for item in self.img:
                self.saveImage(item)

    