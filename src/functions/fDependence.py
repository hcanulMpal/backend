from ..models import db, Dependences

base = db.session

class dbDependence:

    dep = [{ 
        "dependence": 'Palacio',
        "dia_inicial": 'Lunes',
        "dia_final": 'Sabado',
        "hora_inicial": '3:30 p.m',
        "hora_final": '9:30 p.m',
    },
    { 
        "dependence": 'Viejo palacio',
        "dia_inicial": 'Lunes',
        "dia_final": 'Sabado',
        "hora_inicial": '9:30 p.m',
        "hora_final": '5:30 a.m',
    },
    { 
        "dependence": 'Nuevo Palacio',
        "dia_inicial": 'Lunes',
        "dia_final": 'Sabado',
        "hora_inicial": '5:30 a.m',
        "hora_final": '3:30 p.m',
    }]

    def is_Data(self):
        if not Dependences.query.all():
            for item in self.dep:
                self.saveDapendence(item)


    def saveDapendence(self, data):
        dep = Dependences(
            dependence = data['dependence'],
            dia_inicial = data['dia_inicial'],
            dia_final = data['dia_final'],
            hora_inicial = data['hora_inicial'],
            hora_final = data['hora_final'],
        )
        base.add(dep)
        base.commit()

    def finDependence(self, data):
        return Dependences.query.filter_by(dependence=data).first().id

