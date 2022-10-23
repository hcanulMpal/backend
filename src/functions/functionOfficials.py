from ..models import db, Officials
import unicodedata

base = db.session

class dbOfficials:
    
    def setDbOfficials(self, listOficials):
        response  = listOficials
        for item in response['dataFuncionarios']:
            try:
                officials = Officials(
                    id_officials = int(item["id_funcionario"]),
                    name = unicodedata.normalize('NFKD', item["nombre_funcionario"]).encode('ASCII', 'ignore'),
                    semblance = unicodedata.normalize('NFKD', item["semblanza_funcionario"]).encode('ASCII', 'ignore'),
                    url_photo = item["foto_funcionario"],
                    dependence = unicodedata.normalize('NFKD', item["dependencia_funcionario"]).encode('ASCII', 'ignore'),
                    email = item["contacto_funcionario"],
                    status = int(item["status_funcionario"]), 
                )
                base.add(officials)
                base.commit()
            except Exception as error:
                print(error)
        return True