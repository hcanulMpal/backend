from flask_marshmallow import Marshmallow
from dataclasses import fields

ma = Marshmallow()

class schema_Requirements(ma.Schema):
    class Meta:
        fields = ('','','','')

schemaRequi = schema_Requirements()
schemaRequire = schema_Requirements(many=True)
