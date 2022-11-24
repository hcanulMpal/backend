from ..models import db, Tramits
from ..functions import dbDependence

base = db.session

class dbTramits:

    tra = [{
        "tramit": 'Gestion para apoyos funcionales, estudios medicos de especialidad y articulos de primera nesecidad',
        "dependences_id": 'DIF MUNICIPAL'
    },
    {
        "tramit": 'Trabajos de investigacion social',
        "dependences_id": 'DIF MUNICIPAL'
    },
    {
        "tramit": 'Atencion psicologica con sesiones de seguimiento',
        "dependences_id": 'DIF MUNICIPAL'
    },
    {
        "tramit": 'Imparticion de talleres preventivos, formativos y de consientizacion para la salud, prevencion del embarazo en adolecentes, prevencion del consumo de drogas, bulling, valores, maltrato infantil, violencia sexual, fisica, emocional, moral y economica',
        "dependences_id": 'DIF MUNICIPAL'
    },
    {
        "tramit": 'Traslado de pacientes para atencion medica de especialidad',
        "dependences_id": 'DIF MUNICIPAL'
    },
    {
        "tramit": 'Alimentacion a estudiantes foraneos de nivel medio superior y superior, estudiantes indigenas',
        "dependences_id": 'DIF MUNICIPAL'
    },
    {
        "tramit": 'Atencion al adulto mayor con asesoramiento juridico y cuidados preventivos',
        "dependences_id": 'DIF MUNICIPAL'
    },
    {
        "tramit": 'Alimentacion para los primeros 100 dias de vida, distribucion de desayunos frios y calientes, entrega de despensas a poblacion vulnerable',
        "dependences_id": 'DIF MUNICIPAL'
    },
    {
        "tramit": 'Cuidado y atencion de niños/niñas en edad preescolar',
        "dependences_id": 'DIF MUNICIPAL'
    },
    {
        "tramit": 'Corte de cabello basico para la Ciudadania',
        "dependences_id": 'DIF MUNICIPAL'
    },
    {
        "tramit": 'SILLAS DE RUEDAS',
        "dependences_id": 'DIF MUNICIPAL'
    },
    {
        "tramit": 'SILLAS DE RUEDAS PCI',
        "dependences_id": 'DIF MUNICIPAL'
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