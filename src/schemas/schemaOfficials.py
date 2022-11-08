from dataclasses import fields
from flask_marshmallow import Marshmallow

ma = Marshmallow()


#TODO: Declaración de Schema
class Schema_Officials_Organigrama(ma.Schema):
    class Meta:
        fields = ( 'id', 'id_officials', 'name', 'url_photo', 'dependence', 'email', 'id_type' )




#TODO: Instancia de los distintos Schemas
schemaOrganigram = Schema_Officials_Organigrama()
schemaOrganigrams = Schema_Officials_Organigrama(many=True)