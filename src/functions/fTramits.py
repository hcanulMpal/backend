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
    },
    {
        "tramit": 'PASAJES',
        "dependences_id": 'DIF MUNICIPAL'
    },
     {
        "tramit": 'DESPENSAS',
        "dependences_id": 'DIF MUNICIPAL'
    },
     {
        "tramit": 'ROPA Y CALZADO',
        "dependences_id": 'DIF MUNICIPAL'
    },
     {
        "tramit": 'SUETERS',
        "dependences_id": 'DIF MUNICIPAL'
    },
     {
        "tramit": 'APOYO ESCOLAR',
        "dependences_id": 'DIF MUNICIPAL'
    },
    {
        "tramit": 'MOCHILAS ESCOLARES',
        "dependences_id": 'DIF MUNICIPAL'
    },
    {
        "tramit": 'FARDOS DE LAMINAS',
        "dependences_id": 'DIF MUNICIPAL'
    },
    {
        "tramit": 'FUNERALES',
        "dependences_id": 'DIF MUNICIPAL'
    },
    {
        "tramit": 'PROTESIS',
        "dependences_id": 'DIF MUNICIPAL'
    },
     {
        "tramit": 'BOLSAS DE DIALISIS',
        "dependences_id": 'DIF MUNICIPAL'
    },
     {
        "tramit": 'LENTES',
        "dependences_id": 'DIF MUNICIPAL'
    },
     {
        "tramit": 'MEDICAMENTOS',
        "dependences_id": 'DIF MUNICIPAL'
    },
     {
        "tramit": 'COBERTORES',
        "dependences_id": 'DIF MUNICIPAL'
    },
      {
        "tramit": 'ESTUDIOS DE LABORATORIO',
        "dependences_id": 'DIF MUNICIPAL'
    },
      {
        "tramit": 'EST.MED.ESPEC.',
        "dependences_id": 'DIF MUNICIPAL'
    },
      {
        "tramit": 'CONSULTA ESPECIALIZADA',
        "dependences_id": 'DIF MUNICIPAL'
    },
    {
        "tramit": 'AUXILIARES AUDITIVOS',
        "dependences_id": 'DIF MUNICIPAL'
    },
    {
        "tramit": 'BASTONES',
        "dependences_id": 'DIF MUNICIPAL'
    },
    {
        "tramit": 'ANDADERAS ORTOPEDICAS',
        "dependences_id": 'DIF MUNICIPAL'
    },
    {
        "tramit": 'MULETAS',
        "dependences_id": 'DIF MUNICIPAL'
    },
    {
        "tramit": 'ZAPATOS ORTOPEDICOS',
        "dependences_id": 'DIF MUNICIPAL'
    },
    {
        "tramit": 'FAJAS ORTOPEDICOS',
        "dependences_id": 'DIF MUNICIPAL'
    },
      {
        "tramit": 'Apoyo en eventos culturales, tales como: caravanas,domingos culturales, participacion orquesta polifacetica, festivales, taleres, galerias y foros',
        "dependences_id": 'DIRECCION DE CULTURA Y RECREACION MUNICIPAL'
    },
    {
        "tramit": 'Cobros diversos sobre el servicio que ofrecen las diferentes areas',
        "dependences_id": 'DIRECCION DE INGRESOS'
   },
   {
        "tramit": 'Cotizacion de impuesto predial',
        "dependences_id": 'DIRECCION DE INGRESOS'
   },
   {
        "tramit": 'Asesorias y gestion para su licencia de funcionamiento',
        "dependences_id": 'DIRECCION DE INGRESOS'
   },
   {
        "tramit": 'Gestion de tarjetones semifijos',
        "dependences_id": 'DIRECCION DE INGRESOS'
   },
   {
        "tramit": 'Gestion de tarjetones ambulantes',
        "dependences_id": 'DIRECCION DE INGRESOS'
   },
   {
        "tramit": 'Declaraciones por saneamiento ambiental',
        "dependences_id": 'DIRECCION DE INGRESOS'
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
