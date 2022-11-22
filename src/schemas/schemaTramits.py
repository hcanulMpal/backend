from flask_marshmallow import Marshmallow
from dataclasses import fields

ma = Marshmallow()

class schema_Tramits(ma.Schema):
    class Meta:
        fields = ('id','tramit')

schemaTrami = schema_Tramits()
schemaTramit = schema_Tramits(many=True)
