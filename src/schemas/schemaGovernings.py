from dataclasses import fields
from flask_marshmallow import Marshmallow

ma = Marshmallow()


#TODO: Declaracion de Schema
class Schema_Governings(ma.Schema):
    class Meta:
        fields = ('id_governing', 'name', 'semblance', 'url_photo', 'num_governing')


#TODO: INstancia de distintos Schemas
schemaGorvernings= Schema_Governings()
schemasGorvernings= Schema_Governings(many = True)