from dataclasses import fields
from flask_marshmallow import Marshmallow

ma = Marshmallow()

#TODO : Declaracion de Schema
class Schema_Category(ma.Schema):
    class Meta:
        fields = ('id', 'type')


#TODO: Istancia de los distintos Schemas
schemaCa= Schema_Category()
schemaCau = Schema_Category(many=True)
