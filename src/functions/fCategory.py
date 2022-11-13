from ..models import Category, db
from ..schemas.schemaCategory import schemaCa, schemaCau

class dbCategory:

    def setCategory(self):
        return schemaCau.jsonify(Category.query.all())