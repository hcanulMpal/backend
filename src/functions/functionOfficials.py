from ..models import db, Officials
from ..schemas import schemaOrganigram, schemaOrganigrams
import unicodedata

base = db.session

class dbOfficials:


    def is_validate(self):
        if Officials.query.first():
            return True

    
    def setDbOfficials(self, listOficials):
        response  = listOficials
        for item in response['dataFuncionarios']:
            try:
                officials = Officials(
                    id_officials = int(item["id_funcionario"]),
                    name = str(unicodedata.normalize('NFKD', item["nombre_funcionario"]).encode('ASCII', 'ignore').decode()),
                    semblance = str(unicodedata.normalize('NFKD', item["semblanza_funcionario"]).encode('ASCII', 'ignore').decode()),
                    url_photo = item["foto_funcionario"],
                    dependence = str(unicodedata.normalize('NFKD', item["dependencia_funcionario"]).encode('ASCII', 'ignore').decode()),
                    email = item["contacto_funcionario"],
                    status = int(item["status_funcionario"]), 
                )
                base.add(officials)
                base.commit()
            except Exception as error:
                print(error)
        return True


    def setOfficialsOrganigrama(self):
        return schemaOrganigrams.jsonify(Officials.query.all())