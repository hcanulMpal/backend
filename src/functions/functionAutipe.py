from flask import jsonify
from ..models import db,Author, Type
from ..schemas import schemaAu, schemaTy

base = db.session

class list_Type:

    def listType(self):
        Tp = base.query(Author,Type).filter(Author.id_type == Type.id).all()
        Tps = []

        for item in Tp:
            Tps.append([schemaAu.dump(item[0]),
                        schemaTy.dump(item[1])])

        Tps2 = []

        for item in Tps:
            Tps2.append({'id':item[0]['id'],'nombre':item[0]['name'],'telefono':item[0]['mobile'],'email':item[0]['email'],'tipo':item[1]['type']})
 

        try:
             return jsonify({"data": Tps2})
        except Exception as error:
            return jsonify({"error":str(error)}), 500