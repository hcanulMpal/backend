from ..models import db, ENum
from ..schemas import schemaNu, schemaNume

base = db.session

class dbNumero:

    def setNumero(self):
        return schemaNume.jsonify(ENum.query.all())