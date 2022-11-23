from flask_marshmallow import Marshmallow
from dataclasses import fields

ma = Marshmallow()

class schema_Dependence(ma.Schema):
    class Meta:
        fields = ('id','dependence')

schemaDependence = schema_Dependence()
schemaDependences = schema_Dependence(many=True)
