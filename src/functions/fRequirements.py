from ..models import db, Requirements
from .fDependence import dbDependence
from .fTramits import dbTramits

dep = dbDependence()
tra = dbTramits()
base = db.session

class dbRequirements:

    req = [{
        "requirement": 'requirement 1',
        "tramits_id": 'Pago 1',
        "dependences_id": 'Palacio'
    },
    {
        "requirement": 'requirement 2',
        "tramits_id": 'Pago 1',
        "dependences_id": 'Palacio'
    },
    {
        "requirement": 'requirement 3',
        "tramits_id": 'Pago 2',
        "dependences_id": 'Palacio'
    },
    {
        "requirement": 'requirement 4',
        "tramits_id": 'Pago 2',
        "dependences_id": 'Palacio'
    },
    {
        "requirement": 'requirement 5',
        "tramits_id": 'Pago 3',
        "dependences_id": 'Viejo palacio'
    },
    {
        "requirement": 'requirement 6',
        "tramits_id": 'Pago 3',
        "dependences_id": 'Viejo palacio'
    },
    {
        "requirement": 'requirement 7',
        "tramits_id": 'Pago 4',
        "dependences_id": 'Viejo palacio'
    },
    {
        "requirement": 'requirement 8',
        "tramits_id": 'Pago 4',
        "dependences_id": 'Viejo palacio'
    },
    {
        "requirement": 'requirement 9',
        "tramits_id": 'Pago 5',
        "dependences_id": 'Nuevo Palacio'
    },
    {
        "requirement": 'requirement 10',
        "tramits_id": 'Pago 5',
        "dependences_id": 'Nuevo Palacio'
    },
    {
        "requirement": 'requirement 11',
        "tramits_id": 'Pago 6',
        "dependences_id": 'Nuevo Palacio'
    },
    {
        "requirement": 'requirement 12',
        "tramits_id": 'Pago 6',
        "dependences_id": 'Nuevo Palacio'
    }]
    

    def id_Data(self):
        if not Requirements.query.all():
            for item in self.req:
                self.saveRequirement(item)


    def saveRequirement(self, data):
        req = Requirements(
            requirement = data['requirement'],
            tramits_id = dbTramits().findTramits(data['tramits_id']),
            dependences_id = dbDependence().finDependence(data['dependences_id']),
        )
        base.add(req)
        base.commit()

