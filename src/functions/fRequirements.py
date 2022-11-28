from ..models import db, Requirements
from .fDependence import dbDependence
from .fTramits import dbTramits

dep = dbDependence()
tra = dbTramits()
base = db.session

class dbRequirements:

    req = [{
        "requirement": '1',
        "tramits_id": 'Trabajos de investigacion social',
        "dependences_id": 'DIF MUNICIPAL'
    },
    {
        "requirement": 'Requirement 2',
        "tramits_id": 'Trabajos de investigacion social',
        "dependences_id": 'DIF MUNICIPAL'
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

