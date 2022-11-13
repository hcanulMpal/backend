from ..models import Notices, db
from ..schemas.schemaPrensa import schemaPs, schemaPss

class dbPrensa:

    def setPrensa(self):
        return schemaPss.jsonify(Notices.query.all())