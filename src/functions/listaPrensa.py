from flask import jsonify
from ..models import Notices, Author, Category, db
from ..schemas import schemaNoti, schemaAu,schemaCa

base = db.session


class Avisos_list:

    def listAvisos(self):
        Av = base.query(Notices, Author, Category).filter(Notices.id_category == Category.id).filter(Notices.id_author == Author.id).filter(Notices.aprob == True).all()
        Avs =[]

        for item in Av:
            Avs.append([schemaNoti.dump(item[0]),
                       schemaCa.dump(item[2]),
                       schemaAu.dump(item[1])])

        print(Avs, 'Lista')

        try:
             return jsonify({"data": Avs})
        except Exception as error:
            return jsonify({"error":str(error)}), 500