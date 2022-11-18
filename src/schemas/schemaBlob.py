from dataclasses import field
from flask_marshmallow import Marshmallow

ma = Marshmallow()


#TODO Declaracion de Schema
class SchemaBlob(ma.Schema):
    class Meta:
        field = ( 'photo' )


#TODO: Instancia de Clases de schemas Blob
Bl_Schema = SchemaBlob()
Bls_Schema = SchemaBlob(many=True)