from flask import jsonify
from ..models import db, Dependences, Tramits, Requirements
from ..schemas import schemaTramit,schemaDependences,schemaRequire

base = db.session

class listDependencef:

    def listDepen(self):
        Dp = base.query(Dependences, Tramits, Requirements).filter(Requirements.dependences_id == Dependences.id).filter(Requirements.tramits_id == Tramits.id).filter(Requirements ==True).all()
        Dpc = []

        for item in Dp:
            Dpc.append([schemaRequire.dump(item[0]),
                       schemaTramit.dump(item[2]),
                       schemaDependences.dump(item[1])])

       

        try:
             return jsonify({"data": Dpc})
        except Exception as error:
            return jsonify({"error":str(error)}), 500