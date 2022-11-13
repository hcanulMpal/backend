from ..models import Author, db
from ..schemas.schemaAuthor import schemaAu, schemaAus

class dbAuthor:

    def setAuthor(self):
        return schemaAus.jsonify(Author.query.all())