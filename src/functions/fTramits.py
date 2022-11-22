from ..models import db, Tramits
from ..functions import dbDependence

base = db.session

class dbTramits:

    tra = [{
        "tramit": 'Pago 1',
        "dependences_id": 'Palacio'
    },
    {
        "tramit": 'Pago 2',
        "dependences_id": 'Palacio'
    },
    {
        "tramit": 'Pago 3',
        "dependences_id": 'Viejo palacio'
    },
    {
        "tramit": 'Pago 4',
        "dependences_id": 'Viejo palacio'
    },
    {
        "tramit": 'Pago 5',
        "dependences_id": 'Nuevo Palacio'
    },
    {
        "tramit": 'Pago 6',
        "dependences_id": 'Nuevo Palacio'
    }]

    
    def is_Data(self):
        if not Tramits.query.all():
            for item in self.tra:
                self.saveTramits(item)


    def saveTramits(self, data):
        tra = Tramits(
            tramit = data['tramit'],
            dependences_id = dbDependence().finDependence(data['dependences_id'])
        )
        base.add(tra)
        base.commit()

    
    def findTramits(self, data):
        return Tramits.query.filter_by(tramit=data).first().id