from dataclasses import fields
from flask_marshmallow import Marshmallow

ma = Marshmallow()

#TODO : Declaracion de Schema
class Schema_Num(ma.Schema):
    class Meta:
        fields = ('id','name','mobile')


#TODO: Istancia de los distintos Schemas
schemaNu= Schema_Num()
schemaNume = Schema_Num(many=True)