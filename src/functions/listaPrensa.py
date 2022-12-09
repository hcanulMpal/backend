from flask import jsonify
from ..models import db, Notices, Author, Category
from ..schemas import schemaNoti, schemaAu, schemaCa

base = db.session


class Avisos_list:

    def listAvisos(self):
        Av = base.query(Notices, Author, Category).filter(Notices.id_category == Category.id).filter(Notices.id_author == Author.id).filter(Notices.aprob == True).all()
        Avs =[]
        

        for item in Av:
            Avs.append([schemaNoti.dump(item[0]),
                       schemaAu.dump(item[1]),
                       schemaCa.dump(item[2])])

        Avs2 = []

        for item in Avs:
            Avs2.append({'id':item[0]['id'],'titulo':item[0]['title'],'descripcion':item[0]['text'],'imagen':item[0]['url_photo'],'fecha':item[0]['created_date'],'autor':item[1]['name'],'categoria':item[2]['category']})
       

        try:
             return jsonify({"data": Avs2})
        except Exception as error:
            return jsonify({"error":str(error)}), 500