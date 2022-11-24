from flask_marshmallow import Marshmallow
from dataclasses import fields

ma = Marshmallow()

class schema_Dependence(ma.Schema):
    class Meta:
        fields = ('id','dependence','dia_inicial', 'dia_final', 'hora_inicial', 'hora_final','lat','long')

schemaDependence = schema_Dependence()
schemaDependences = schema_Dependence(many=True)
