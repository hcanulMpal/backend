import unicodedata
from ..models import db, Token, Governings, Officials
import requests

base = db.session

class fTocken:
   
    def validToken(self):
        resp = base.query(Token).order_by(Token.created_date.desc()).first()
        print(resp)
        if resp is not None:
            if resp.count_date > 0:
                token = resp.code
            else:
                token = self.getToken()
        else:
                token = self.getToken()
        return token


    def getToken(self):
        response = requests.post("https://apicarrillo.felipecarrillopuerto.gob.mx/api/Keys/generate")
        data = response.json()
        if data['status']:
            token = Token(
                code = data['token'],
                final_date = data['expira'],
                count_date = 30,
            )
            base.add(token)
            base.commit()
        return data['token']


    def getOfficials(self):
        response = requests.get("https://apicarrillo.felipecarrillopuerto.gob.mx/api/funcionarios/get_all?API_KEY_FCP=" + str(self.validToken()))
        return response


    def getGovernings(self):
        response = requests.get("https://apicarrillo.felipecarrillopuerto.gob.mx/api/regidores/get_all?API_KEY_FCP=" + str(self.validToken()))
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

