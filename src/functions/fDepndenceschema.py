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

    
        Dpc2 = []

        for item in Dpc:
            Dpc2.append({'id':item[0]['id'], 'tramites':item[1]['tramit'],'requerimientos':item[0]['requirement'],'dependencia':item[2]['dependence'],'latitud':item[2]['lat'],'longitud':item[2]['long'],'Hora inicial':item[2]['hora_inicial'],'Hora final':item[2]['hora_final'],'Dia inicial':item[2]['dia_inicial'],'Dia final':item[2]['dia_final']})

       

        try:
             return jsonify({"data": Dpc2})
        except Exception as error:
            return jsonify({"error":str(error)}), 500