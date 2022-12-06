from dataclasses import fields
from flask_marshmallow import Marshmallow

ma = Marshmallow()

#TODO : Declaracion de Schema
class Schema_Img_Ctegory(ma.Schema):
    class Meta:
        fields = ('id','categorys','created_date')


#TODO: Istancia de los distintos Schemas
schemaImgC = Schema_Img_Ctegory()
schemaImgsC = Schema_Img_Ctegory(many=True)