
from ..models import db, Type

base = db.session

class fType():

    def dbauto(self):
        lista =['Nombramientos', 'Directores', 'Coordinadores', 'Jefes de departamento']
        for i in lista:
            tipo = Type(type=i)
            base.add(tipo)
            base.commit()