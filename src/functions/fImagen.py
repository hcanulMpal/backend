from flask import jsonify
from ..models import Imagen,db, ImgCategory
from ..schemas import schemaImg, schemaImgs

base = db.session

class ImagesList:

    def listImages(self):
        IM = base.query(Imagen).filter(Imagen.imgCategory_id == ImgCategory.id).filter(Imagen == True).all()
        Ims = []

        for item in IM:
            Ims.append([schemaImg.dump(item[0])])


        try:
             return jsonify({"data": Ims})
        except Exception as error:
            return jsonify({"error":str(error)}), 500



            
