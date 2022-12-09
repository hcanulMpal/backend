from ..models import db, Author, Type
from .governingsType import fType
from ..schemas import schemaAu, schemaAus

base = db.session


class dbAuthor:

    def setAuthor(self):
        return schemaAus.jsonify(Author.query.all())
        

class fAuth:

    pedro = {
        "name": 'Pedro Pony',
        "mobile": '9862345654', 
        "email": 'pedroponyproplayerinsano@gmail.com', 
        "id_type": 'Directores',
        }
    
    manuel = {
        "name": 'Manuel Chan',
        "mobile": '9831235665', 
        "email": 'manuelchan@gmail.com', 
        "id_type": 'Directores',
        }
    armando = {
        "name": 'Armando Angulo',
        "mobile": '9831256787', 
        "email": 'armandoangulo@gmail.com', 
        "id_type": 'Directores',
        }

    def is_Data(self):
        if not Author.query.all():
            self.saveAuthors(self.pedro)
            self.saveAuthors(self.manuel)
            self.saveAuthors(self.armando)
        
    
    def saveAuthors(self, data):
        auth = Author(
            name = data['name'],
            mobile = data['mobile'],
            email = data['email'],
            id_type = fType().findAuthorType(data['id_type']),
        )
        base.add(auth)
        base.commit()
    
    def findNoticesAuthor(self, name):
        return Author.query.filter_by(name=name).first().id
