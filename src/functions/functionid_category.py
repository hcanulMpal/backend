from ..models import db, ImgCategory
from ..schemas import schemaImgC,schemaImgsC

base = db.session

class dbImgId_Category:

    def setId_Category(self):
        return schemaImgsC.jsonify(ImgCategory.query.all())