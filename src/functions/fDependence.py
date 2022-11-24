from ..models import db, Dependences

base = db.session

class dbDependence:

    dep = [{ 
        "dependence": 'DIF MUNICIPAL',
        "dia_inicial": 'Lunes',
        "dia_final": 'Viernes',
        "hora_inicial": '8:00 a.m',
        "hora_final": '3:00 p.m',
        "ubi_lat": '123.456',
        "ubi_long": '123.456',
    },
    { 
        "dependence": 'DIRECCION DE TURISMO MUNICIPAL',
        "dia_inicial": 'Lunes',
        "dia_final": 'Viernes',
        "hora_inicial": '8:00 a.m',
        "hora_final": '3:00 p.m',
        "ubi_lat": '123.456',
        "ubi_long": '123.456',
    },
    { 
        "dependence": 'DIRECCION DE CULTURA Y RECREACION MUNICIPAL',
        "dia_inicial": 'Lunes',
        "dia_final": 'Viernes',
        "hora_inicial": '8:00 a.m',
        "hora_final": '3:00 p.m',
        "ubi_lat": '123.456',
        "ubi_long": '123.456',
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
            ubi_lat = data['ubi_lat'],
            ubi_long = data['ubi_long']
        )
        base.add(dep)
        base.commit()

    def finDependence(self, data):
        return Dependences.query.filter_by(dependence=data).first().id

