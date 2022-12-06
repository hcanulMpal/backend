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

        Ims2 = []

        for item in Ims:
            Ims2.append({'id':item[0]['id'],'url':item[0]['url_photo'],'descripcion':item[0]['description'],'categoria':item[1]['categorys'],'fecha':item[1]['created_date']})
                       


        try:
             return jsonify({"data": Ims2})
        except Exception as error:
            return jsonify({"error":str(error)}), 500



            
