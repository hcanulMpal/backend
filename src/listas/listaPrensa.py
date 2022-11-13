from flask import jsonify
from models import Notices, Author, Category, db
from schemas import schemaNotices, schemaAuthor,schemaCategory

base = db.session


class Avisoss:

    data = {

    }

    def listAvisos(self):
        Av = base.query(Notices, Author, Category).filter(Notices.id_category == Category.id).filter(Notices.id_Author == Author.id).filter(Notices = True).all()
        Avs =[]

        for item in Av:
            Avs.append(schemaNotices(item[0]), schemaCategory(item[1]),schemaAuthor(item[2]))

        try:
             return jsonify({"data": Avs}), 200
        except Exception as error:
            return jsonify({"error":str(error)}), 500

                	 
        
   	