from ..models import db, Token
import requests

base = db.session

class fTocken:
   
    def validToken(self):
        resp = base.query(Token).order_by(Token.created_date.desc()).first()
        resp = 0
        if resp > 0:
            token = resp.token
        else:
            token = self.getToken()
        return token


    def getToken(self):
        response = requests.post("https://apicarrillo.felipecarrillopuerto.gob.mx/api/Keys/generate")
        data = response.json()
        print(data)
        if data['status']:
            token = Token(
                code = data['token'],
                final_date = data['expira'],
                count_date = 30,
            )
            base.add(token)
            base.commit()
        return data['token']


    def getFuncionarios(self):
        response = requests.get("https://apicarrillo.felipecarrillopuerto.gob.mx/api/funcionarios/get_all?API_KEY_FCP=" + str(self.validToken()))
        return response


    def getRegidores(self):
        response = requests.get("https://apicarrillo.felipecarrillopuerto.gob.mx/api/regidores/get_all?API_KEY_FCP=" + str(self.validToken()))
        return response


    def setDbFuncionarios(self):
        response  = self.getFuncionarios()
        for item in response.json()['dataFuncionarios']:
            print(item['nombre_funcionario'].encode('utf-8'))
            print(item['foto_funcionario'].encode('utf-8'))
            print(item['dependencia_funcionario'].encode('utf-8'))
            print(item['contacto_funcionario'].encode('utf-8'))