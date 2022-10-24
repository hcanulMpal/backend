
from ..models import db, Token
import requests

base = db.session

class fTocken:

   
    def validToken(self):
        resp = base.query(Token).order_by(Token.created_date.desc()).first()
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


    

