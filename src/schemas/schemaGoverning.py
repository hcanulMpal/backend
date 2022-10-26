from dataclasses import fields
from flask_marshmallow import Marshmallow

ma = Marshmallow()


class SchemaGovernings(ma.Schema):
    class Meta:
        fields = ( 'id_governing', 'name', 'semblance', 'url_photo', 'num_governing' )




#TODO: Instancia de Clases de schemas governings

gbo_Schema = SchemaGovernings()
gbos_Schema = SchemaGovernings(many=True)