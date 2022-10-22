from flask_marshmallow import Marshmallow
from dataclasses import fields

ma = Marshmallow()


class OfficialsSchema(ma.Schema):
    class meta():
        fields=("id", "id_officials ", "name", "semblance", "url_photo", "dependence"
        , "email", "status", "created_date", "update_on")


class  GoverningsSchema(ma.Schema):
    class meta():
        fields=("id", "id_officials ", "name", "semblance", "url_photo", "dependence"
        , "email", "status", "created_date", "update_on")



Official_Schema=OfficialsSchema()
Officials_Schema=OfficialsSchema(many=True)

Governing_Schema=GoverningsSchema()
Governings_Schema=GoverningsSchema(many=True)















