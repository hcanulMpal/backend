from dataclasses import fields
from flask_marshmallow import Marshmallow

ma = Marshmallow()

#TODO : Declaracion de Schema
class Schema_Prensa(ma.Schema):
    class Meta:
        fields = ('id_category', 'id_author',)


#TODO: Istancia de los distintos Schemas
schemaPs = Schema_Prensa()
schemaPss = Schema_Prensa(many=True)