from ..models import db, Officials
from ..schemas import schemaOrganigram, schemaOrganigrams
import unicodedata

base = db.session

class dbOfficials:


    def is_validate(self):
        if Officials.query.first():
            return True

    
    def setDbOfficials(self, listOficials):
        response  = listOficials
        nombramientos = [
            'SECRETARIA GENERAL',
            'TESORERO MUNICIPAL',
            'CONTRALORA MUNICIPAL',
            'OFICIAL MAYOR',
            'SECRETARIO PARTICULAR',
            'OFICIAL 01 DEL REGISTRO CIVIL',
            'SECRETARIO TECNICO',
            'DELEGADA DE LA PROCURADURIA DEPROTECCION DE NINAS, NINOS Y ADOLESCENTES.',
            'SECRETARIO PRIVADO'
        ]
        for item in response['dataFuncionarios']:
            try:
                cargo = 0
                dependencia = str(unicodedata.normalize('NFKD', item["dependencia_funcionario"]).encode('ASCII', 'ignore').decode()),
                if dependencia[0].startswith('DIRECTOR'):
                    cargo = 2
                elif dependencia[0].startswith('COORDINADOR'):
                    cargo = 3
                elif dependencia[0].startswith('JEF'):
                    cargo = 4
                else:
                    for i in nombramientos:
                        if dependencia[0] == i:
                            cargo = 1
                print(cargo, dependencia[0])
                officials = Officials(
                    id_officials = int(item["id_funcionario"]),
                    name = str(unicodedata.normalize('NFKD', item["nombre_funcionario"]).encode('ASCII', 'ignore').decode()),
                    semblance = str(unicodedata.normalize('NFKD', item["semblanza_funcionario"]).encode('ASCII', 'ignore').decode()),
                    url_photo = item["foto_funcionario"],
                    dependence = dependencia[0],
                    email = item["contacto_funcionario"],
                    status = int(item["status_funcionario"]),
                    id_type =  cargo,
                )
                base.add(officials)
                base.commit()
            except Exception as error:
                print(error)
        return True


    def setOfficialsOrganigrama(self):
        return schemaOrganigrams.jsonify(Officials.query.all())


    def updateOficials(self, data):
        try:
            Officials.query.filter_by(dependence=data).update({'id_type':1})
            base.commit()
            return True
        except Exception as error:
            print(error)
            return False
