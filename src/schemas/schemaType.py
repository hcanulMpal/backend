from flask_marshmallow import Marshmallow
from dataclasses import fields

ma = Marshmallow()

class schema_Type(ma.Schema):
    class Meta:
        fields = ('id','type')

schemaTy = schema_Type()
schemaTyp = schema_Type(many=True)
