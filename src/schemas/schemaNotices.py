from dataclasses import fields
from flask_marshmallow import Marshmallow

ma = Marshmallow()


#TODO: Declaracion de Schema
class Schema_Notices_Organigrama(ma.Schema):
    class Meta:
        fields = ('id','title','text','url_photo','created_date')


#TODO: Instancia de los distintos Schemas
schemaNoti = Schema_Notices_Organigrama()
schemaNotis = Schema_Notices_Organigrama(many=True) 