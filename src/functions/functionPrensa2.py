from flask import jsonify
from ..models import db, Notices, Author
from ..schemas import schemaNoti, schemaAu

base = db.session


class Avisos_list2:

    def listAvisos2(self):
        Av2 = base.query(Notices, Author).filter().filter(Notices.id_author == Author.id).filter(Notices.aprob == True).all()
        Avs2 =[]
        

        for item in Av2:
            Avs2.append([schemaNoti.dump(item[0]),
                       schemaAu.dump(item[1])])

        Avs3 = []

        for item in Avs2:
            Avs3.append({'id':item[0]['id'],'titulo':item[0]['title'],'descripcion':item[0]['text'],'imagen':item[0]['url_photo'],'fecha':item[0]['created_date'],'autor':item[1]['name']})
       

        try:
             return jsonify({"data": Avs3})
        except Exception as error:
            return jsonify({"error":str(error)}), 500