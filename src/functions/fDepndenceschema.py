from flask import jsonify
from ..models import db, Dependences, Tramits, Requirements
from ..schemas import schemaTrami,schemaDependence,schemaRequi

base = db.session

class listDependencef:

    def listDepen(self):
        Dp = base.query(Dependences, Tramits, Requirements).filter(Requirements.dependences_id == Dependences.id).filter(Requirements.tramits_id == Tramits.id).all()
        Dpc = []

        for item in Dp:
            Dpc.append([schemaRequi.dump(item[2]),
                       schemaTrami.dump(item[1]),
                       schemaDependence.dump(item[0])])

       

        try:
             return jsonify({"data": Dpc})
        except Exception as error:
            return jsonify({"error":str(error)}), 500