import unicodedata
from ..models import db, Officials
from .functionToken import fTocken
import requests

FuncT = fTocken()
base = db.session

class fOfficials:

    def getOfficials(self):
        response = requests.get("https://apicarrillo.felipecarrillopuerto.gob.mx/api/funcionarios/get_all?API_KEY_FCP=" + str(FuncT.validToken()))
        return response


    def setDbOfficials(self):
        response  = self.getOfficials()
        for item in response.json()['dataFuncionarios']:
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
        print("Base de Datos Actualizada")
        return "Base de Datos Actualizada", 200