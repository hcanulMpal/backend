from ..models import db, Dependences

base = db.session

class dbDependence:

    dep = [{ 
        "dependence": 'DIF MUNICIPAL',
        "dia_inicial": 'Lunes',
        "dia_final": 'Viernes',
        "hora_inicial": '8:00 a.m',
        "hora_final": '3:00 p.m',
        "lat": '19.578502437996626',
        "long": '-88.04547660314498',
    },
    { 
        "dependence": 'DIRECCION DE TURISMO MUNICIPAL',
        "dia_inicial": 'Lunes',
        "dia_final": 'Viernes',
        "hora_inicial": '8:00 a.m',
        "hora_final": '3:00 p.m',
        "lat": '19.575314',
        "long": '-88.044821',
    },
    { 
        "dependence": 'DIRECCION DE CULTURA Y RECREACION MUNICIPAL',
        "dia_inicial": 'Lunes',
        "dia_final": 'Viernes',
        "hora_inicial": '8:00 a.m',
        "hora_final": '3:00 p.m',
        "lat": '19.5836223',
        "long": '-88.0430042',
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
            lat = data['lat'],
            long = data['long']
        )
        base.add(dep)
        base.commit()

    def finDependence(self, data):
        return Dependences.query.filter_by(dependence=data).first().id

