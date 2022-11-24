from flask import jsonify
from ..models import Imagen,db, ImgCategory
from ..schemas import schemaImg, schemaImgC

base = db.session

class ImagesList:

    def listImages(self):
        IM = base.query(Imagen, ImgCategory).filter(Imagen.imgCategory_id == ImgCategory.id).all()
        Ims = []

        for item in IM:
            Ims.append([schemaImg.dump(item[0]),
                       schemaImgC.dump(item[1])])
                       


        try:
             return jsonify({"data": Ims})
        except Exception as error:
            return jsonify({"error":str(error)}), 500



            
