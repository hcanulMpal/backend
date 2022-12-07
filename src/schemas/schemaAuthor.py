from dataclasses import fields
from flask_marshmallow import Marshmallow

ma = Marshmallow()

#TODO : Declaracion de Schema
class Schema_Author(ma.Schema):
    class Meta:
        fields = ('id','name','mobile','email','id_type')


#TODO: Istancia de los distintos Schemas
schemaAu= Schema_Author()
schemaAus = Schema_Author(many=True)