from ..models import Notices, db, Governings
from ..schemas.schemaNotices import schemaNoti, schemaNotis
from ..functions.fAuthor import fAuth
from ..functions.fCategory import funcCat

base = db.session

class dbNotices:

    n1 = {
        "title": 'AMLO pedirá perdón a los pueblos mayas en Tihosuco',
        "text": 'AMLO pedirá perdón a los pueblos mayas en Tihosuco, este poblado cuna de esta cultura en Quintana Roo, será el escenario en donde el presidente de México, Andrés Manuel López Obrador, encabezará la ceremonia de petición de perdón a los pueblos mayas por los agravios cometidos durante la lucha social maya.\r\nLa resistencia del pueblo maya en la defensa de sus medios de vida, la milpa, la lengua maya, la cultura, su territorio en sí, fue lo que desencadenó la mal nombrada “Guerra de Castas” de 1847.\r\nTe Puede Interesar: Preparan Foro Regional de Consulta a los pueblos mayas\r\nDicha ceremonia se realizará el próximo 3 de mayo en Tihosuco, lugar decretado recientemente como sitio de monumentos históricos a cargo del Instituto Nacional de Antropología e Historia (INHA).\r\nEl evento obedece a los 500 años de resistencia indígena, y el pueblo de uno de los personajes de esta lucha social maya, Jacinto Pat, ha sido elegido para este acontecimiento.',
        "id_category": 'Politica', 
        "id_author": 'Manuel Chan', 
        "url_photo": 'https://turquesanews.mx/wp-content/uploads/2021/04/Tihosuco.jpg.webp',
    }
    n2 = {
        "title":'Escape de abejas en zona maya moviliza a elementos de protección civil', 
        "text": 'El reporte del escape de un enjambre de abejas en un domicilio de céntrica avenida en Felipe Carrillo Puerto, movilizó a elementos de la Dirección de Protección Civil.\r\nQuines realizaron un despliegue encaminado a proteger a la ciudadanía de la picadura de las furibundas abejas.\r\nTe Puede Interesar: Buscan fortalecer apicultura de la Zona Maya\r\nMinutos más tarde, arribaron al lugar mencionado, elementos de protección civil con el equipo correspondiente, y rescataron seis colmenas de abejas que habían iniciado enjambrazón.\r\nDichas colmenas fueron trasladadas fuera de la ciudad puesto que representan un peligro tenerlos en casa, aún más en esta temporada de calor, y debido a la protección natural que tienen las abejas de defender su alimento, la miel.',
        "id_category": 'Sociedad', 
        "id_author": 'Manuel Chan', 
        "url_photo": 'https://turquesanews.mx/wp-content/uploads/2021/04/Abejas-ataque.jpg.webp',
    }
    n3 = {
        "title": 'Mujeres artesanas mayas piden reactivar la economía de sus comunidades',
        "text": 'La pandemia por el Covid-19 ha complicado una de las actividades artesanales de mujeres mayas que fortalecían la economía local; por ello es urgente reactivarlo, señaló Fernanda Cen Angulo, artesana de Chancah Derrepente.\r\nEl arte popular al que se dedican es la cestería con bejuco, la cual obtienen de la selva maya de esta región, y que cada día es difícil de conseguir.\r\n\r\nEstas obras, que moldean con sus propias manos, son destinadas principalmente a la zona turística de la entidad.\r\n“La situación era difícil sin pandemia, después de más de un año se ha complicado aún más, y es urgente que se reactive”, señaló en lengua maya doña Fernanda Cen Angulo. Agregó que la actividad artesanal a la que se dedican varias familias están resintiendo los efectos de la pandemia por Covid-19, por ello la urgencia de reactivar la economía local.\r\n\r\nUna de las comunidades pioneras en este arte es la comunidad de Kopchen, localizada en esta misma zona de comunidades rurales de Felipe Carrillo Puerto, y una de sus precursoras es la artesana Rosalinda Cahuich, quien ha obtenido destacados premios municipales, estatales y nacionales.\r\nAdemás de generar empleo en la comunidad a través de este arte popular que consiste en la cestería a base de bejuco.',
        "id_category": 'Cultura', 
        "id_author": 'Manuel Chan', 
        "url_photo": 'https://turquesanews.mx/wp-content/uploads/2021/04/WhatsApp-Image-2021-04-19-at-8.14.40-AM-1.jpeg.webp',
    }
    n4 = {
        "title": 'Reclaman pago delegados de comunidades rurales de Felipe Carrillo Puerto',
        "text": 'Manifiestan inconformidad autoridades comunitarias del municipio de Felipe Carrillo Puerto, debido a la falta de pago a sus quincenas.\r\nSubdelegados, delegados y alcaldes no ha recibido el pago correspondiente a la primera quincena de este mes de abril.\r\nEl subdelegado de la comunidad de Francisco I. Madero, Emeterio Che Che indicó que no es la primera vez que se atrasa el pago, se ha vuelto recurrente las mentiras del gobierno de José Esquivel Vargas.\r\n“No hay respuesta para el pago de nuestras quincenas, siempre nos mienten, por eso estamos aquí para escuchar que nos va a decir hoy”, señaló en lengua maya el subdelegado.\r\nEntrevistado en la sala de espera para que el secretario general Dalton Gómez les explique a qué debe el atraso a sus pagos, el subdelegado de la zona de Los Chunes, indicó que a cada autoridad le deben alrededor de mil pesos.\r\nSon más de 80 autoridades comunitarias las que no han recibido el pago de sus quincenas y a más de 13 horas de espera no habían sido atendidos en el palacio municipal de Felipe Carrillo Puerto.',
        "id_category": 'Economia',
        "id_author": 'Pedro Pony',
        "url_photo": 'https://turquesanews.mx/wp-content/uploads/2021/04/WhatsApp-Image-2021-04-16-at-2.08.15-PM.jpeg.webp',
    }
    n5 = {
        "title": 'Extienden fecha de vacunación covid-19 en zona maya',
        "text": 'Extienden fecha de vacunación covid-19 en zona maya, se extendió por un día más la aplicación de la segunda dosis de la vacuna contra el coronavirus en Felipe Carrillo Puerto.\r\nLas autoridades de salud convocaron a las personas de 60 a 69 años de edad y que ya recibieron la primera dosis, acudir a los puestos de vacunación de la cabecera municipal.\r\nTe Puede Interesar: Zona Maya a punto de finalizar vacunación covid de adultos mayores\r\nDe acuerdo con el doctor Alfredo Hernández Gonzáles, hasta este miércoles son, 4,845 dosis aplicadas de 5,164 que deben aplicarse a personas de la tercera edad que ya recibieron la primera dosis.\r\nEl también director de salud municipal, Hernández Gonzáles, indicó que falta por aplicarse, 319 dosis, para completar la meta en Felipe Carrillo Puerto\r\nPor ello es importante que los adultos mayores que ya recibieron la primera dosis acudan al puesto de vacunación del domo deportivo de la colonia Cecilio Chi y completar esta protección contra el coronavirus.\r\n\r\nRecalcó que la siguiente etapa de vacunación será para la población de 50 a 59 años de edad y será durante el mes de mayo, tiempo en el cual podrá aplicarse la dosis a aquellos adultos mayores de 60 años y más que por algún motivo no lograron recibir el biológico.',
        "id_category": 'Salud',
        "id_author": 'Armando Angulo',
        "url_photo": 'https://turquesanews.mx/wp-content/uploads/2021/04/Vacunacion-zona-maya-1.jpg.webp',
    }
    n6 = {
        "title": 'Desabasto de maíz en la comunidad maya de Santa Rosa',
        "text": 'En Santa Rosa, municipio de Felipe Carrillo Puerto, familias mayas vuelven a lanzar un llamado a las autoridades ante el desabasto de maíz; hace un mes que las tiendas Diconsa no cuentan con este alimento básico.\r\nEl encargado de la tienda de Seguridad Alimentaria Segalmex, ha informado a los habitantes de la comunidad que para el mes de mayo se espera que vuelvan a contar con maíz, por lo que temen que ahora aumenten los precios.\r\nActualmente, el precio del maíz está entre 255 a 257 pesos el costal de 50 kilogramos en las tiendas Diconsa de las comunidades.\r\nAnte esta situación, el exdelegado de la comunidad de Santa Rosa, Baldomero Poot Pat, dijo sentirse abandonado por los tres niveles de Gobierno y aún más por el presidente municipal José Esquivel Vargas, alias “Chak Meex”.\r\nSeñaló que la autoridad municipal debería gestionar ante las instancias correspondientes para que lo más pronto posible pueda atenderse este problema de desabasto en la comunidad de Santa Rosa.',
        "id_category": 'Economia',
        "id_author": 'Manuel Chan',
        "url_photo": 'https://turquesanews.mx/wp-content/uploads/2021/04/WhatsApp-Image-2021-04-14-at-7.23.33-AM-1.jpeg.webp',
    }
    n7 = {
        "title": 'Zona Maya a punto de finalizar vacunación covid de adultos mayores',
        "text": 'Zona Maya a punto de finalizar vacunación covid de adultos mayores, el doctor Alfredo Hernández Gonzáles dio a conocer que se han aplicado 4,251 de 5,126 dosis de la vacuna contra el coronavirus a adultos mayores del municipio de Felipe Carrillo Puerto.\r\nLa estrategia de aplicación implementada para cumplir con la meta durante los días 9 al 13 de abril, fue destinar autobuses para el traslado de adultos mayores de sus comunidades a los puestos de vacunación mencionados.\r\nTe Puede Interesar: Aplican segunda dosis de vacuna covid-19 en zona maya\r\nDe acuerdo con el calendario dado a conocer por las autoridades de salud, la aplicación de la dosis se lleva a cabo en el puesto de vacunación establecido en el domo deportivo de la colonia Cecilio Chi.\r\nEste martes es el último día de aplicación y corresponde a personas de la tercera edad de las comunidades de Tepich, Tihosuco, Señor y X- Pichil.\r\nEl también director de salud municipal, Alfredo Hernández, indicó que la protección de este sector vulnerable de la población se atiende con la coordinación de las autoridades de salud, el gobierno federal, estatal y municipal.\r\nPor último, agregó que la siguiente etapa de vacunación será para la población de 50 a 59 años de edad y será durante el mes de mayo.',
        "id_category": 'Salud',
        "id_author": 'Manuel Chan',
        "url_photo": 'https://turquesanews.mx/wp-content/uploads/2021/04/Vacunacion-zona-maya.jpg.webp',
    }
    n8 = {
        "title": 'Auto “fantasma” arrolla a campesino en zona maya',
        "text": 'Auto “fantasma” arrolla a campesino en zona maya, un agricultor murió luego de ser atropellado cuando se transportaba a su milpa en bicicleta.\r\nEl percance ocurrió la madrugada de este lunes a 10 kilómetros de Felipe Carrillo Puerto en la carretera que conduce a Chetumal.\r\nTe puede Interesar: Aumentan accidentes en la Zona Maya por la Semana Santa\r\nEl reporte de un cuerpo tirado a orilla de la carretera federal y una bicicleta destrozada, fue realizado por los automovilistas que cruzaban por el lugar.\r\nEl responsable del accidente huyó del lugar y no pudo ser identificado.\r\nMás tarde acudieron autoridades ministeriales para las investigaciones correspondientes y el levantamiento del cuerpo del campesino.',
        "id_category": 'Accidente',
        "id_author": 'Pedro Pony',
        "url_photo": 'https://turquesanews.mx/wp-content/uploads/2021/04/Atropellado-zona-maya.jpg.webp',
    }
    n9 = {
        "title": 'En Felipe Carrillo Puerto muere comandante maya en Centro Ceremonial',
        "text": 'El comandante maya, Florentino Ay Nahuat, originario de Tuzik, fue hallado muerto ayer domingo en el Centro Ceremonial la Cruz Parlante de Felipe Carrillo Puerto.\r\nUna ambulancia de la Cruz Roja arribó al Centro Ceremonial y minutos después, paramédicos confirmaron que el comandante maya de alrededor de 70 años ya no contaba con signos vitales.\r\nHasta el momento se desconoce la causa de su muerte; familiares cercanos al comandante informaron que no estaba enfermo.\r\nPosteriormente, arribaron elementos policiacos al Centro Ceremonial y más tarde la Policía Ministerial para las labores correspondientes.\r\nEl también campesino, recién había participado en la alborada para la fiesta tradicional de la comunidad, ceremonia dedicada a los santos patronos conocido como (Las tres personas) de los Centros Ceremoniales de Chumpón, Tixcacal Guardia y Tulum.',
        "id_category": 'Sociedad',
        "id_author": 'Pedro Pony',
        "url_photo": 'https://turquesanews.mx/wp-content/uploads/2021/04/muere-comandante-maya.jpeg.webp',
    }
    n10 = {
        "title": 'Tubería dañada deja sin agua a cientos de familias en Felipe Carrillo Puerto',
        "text": 'Cientos de familias de diversas colonias de Felipe Carrillo Puerto siguen padeciendo por falta de agua potable, debido a una tubería dañada.\r\nDesde el viernes pasado se ha estado presentando este problema por baja presión y falta de agua, en por lo menos siete colonias de esta cabecera municipal.\r\nDe acuerdo a un informe de la Comisión de Agua Potable y Alcantarillado (CAPA), la falta de agua es debido a una nueva fuga en la línea de conducción de 12 pulgadas, ubicada en la avenida Constituyentes, entre las calles 43 y 45 de la colonia Juan Bautista Vega, por lo que el servicio de agua potable estará interrumpido durante el transcurso de este lunes.\r\nLas colonias que resultarán más afectadas ante esta situación son la colonia Centro, Martínez Ross, Wuayumil, Juan Bautista Vega, Javier Rojo Gómez, Emiliano Zapata, Cecilio Chi y parte de Lázaro Cárdenas y Rafael E. Melgar.',
        "id_category": 'Accidente',
        "id_author": 'Manuel Chan',
        "url_photo": 'https://turquesanews.mx/wp-content/uploads/2021/04/WhatsApp-Image-2021-04-12-at-8.15.56-AM-1.jpeg.webp',
    }
    n11 = {
        "title": '171 Aniversario de la fundación de la ciudad de Felipe Carrillo Puerto',
        "text": 'Estamos en la celebración del 171 Aniversario de la fundación de la Ciudad de Felipe Carrillo Puerto. Esta mañana recibimos en la plaza pública a la presidenta municipal Mary Hernández, en compañía de la presidenta municipal de Benito Juárez, Mara Lezama; el presidente municipal de José María Morelos, Erik Borges Yam; a todos los regidores y parte del equipo del H. Ayuntamiento, para inaugurar esta fiesta municipal que se llevará a cabo este fin de semana.',
        "id_category": 'Presidencia',
        "id_author": 'Pedro Pony',
        "url_photo": 'https://www.felipecarrillopuerto.gob.mx/images/noticias/2021/2021101601.jpg',
    }
    n12 = {
        "title": 'Visita de las instalaciones del DIF Carrillo Puerto',
        "text": 'Mary Hernández, Presidenta Municipal de Felipe Carrillo Puerto, trabaja fuertemente para mejorar la calidad y el servicio que brinda el Sistema para el Desarrollo Integral de la Familia (DIF Felipe Carrillo Puerto). En esta nueva transformación se necesita impulsar el altruismo e implementar estrategias en materia de asistencia social, bienestar familiar, perspectiva de género, entre otros temas. El día de hoy, la alcaldesa recorrió las instalaciones del DIF Municipal para conocer sus principales necesidades. Estuvo en compañía de la Presidenta Honoraria, Maria Del Carmen Solsan, así como de las diferentes autoridades de dicha instancia.',
        "id_category": 'Presidencia',
        "id_author": 'Pedro Pony',
        "url_photo": 'https://www.felipecarrillopuerto.gob.mx/images/noticias/2021/2021101202.jpg',
    }

    def is_validate(self):
        if not Notices.query.all():
            self.saveNotices(self.n1)
            self.saveNotices(self.n2)
            self.saveNotices(self.n3)
            self.saveNotices(self.n4)
            self.saveNotices(self.n5)
            self.saveNotices(self.n6)
            self.saveNotices(self.n7)
            self.saveNotices(self.n8)
            self.saveNotices(self.n9)
            self.saveNotices(self.n10)
            self.saveNotices(self.n11)
            self.saveNotices(self.n12)

    
    def saveNotices(self, data):
        noti = Notices(
            title = data['title'],
            text = data['text'],
            id_category = funcCat().findNoticesCategory(data['id_category']),
            id_author = fAuth().findNoticesAuthor(data['id_author']),
            url_photo = data['url_photo']
        )
        base.add(noti)
        base.commit()
        return print(noti)


    def setNotices(self):
        return schemaNotis.jsonify(Notices.query.all())