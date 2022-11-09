from ..models import Notices, db, Governings
from ..schemas.schemaNotices import schemaNoti, schemaNotis

class dbNotices:

    def setNotices(self):
        return schemaNotis.jsonify(Notices.query.all())