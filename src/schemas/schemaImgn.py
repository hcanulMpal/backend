from dataclasses import fields
from flask_marshmallow import Marshmallow

ma = Marshmallow()

#TODO : Declaracion de Schema
class Schema_Img(ma.Schema):
    class Meta:
        fields = ('id','url_photo','description','imgCategory_id')


#TODO: Istancia de los distintos Schemas
schemaImg = Schema_Img()
schemaImgs = Schema_Img(many=True)