from ..models import db, Dependences

base = db.session

class dbDependence:

    dep = [{ 
        "dependence": 'Palacio',
        "schedules": 'Lunes a viernes (6:00 p.m a 9:a.m)'
    },
    { 
        "dependence": 'Viejo palacio',
        "schedules": 'Lunes a viernes (9:00 a.m a 1:p.m)'
    },
    { 
        "dependence": 'Nuevo Palacio',
        "schedules": 'Lunes a viernes (1:00 p.m a 6:p.m)'
    }]

    def is_Data(self):
        if not Dependences.query.all():
            for item in self.dep:
                self.saveDapendence(item)


    def saveDapendence(self, data):
        dep = Dependences(
            dependence = data['dependence'],
            schedules = data['schedules']
        )
        base.add(dep)
        base.commit()

    def finDependence(self, data):
        return Dependences.query.filter_by(dependence=data).first().id