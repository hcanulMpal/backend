from ..models import db, Governings
import unicodedata

base = db.session

class dbGovernings:

    def setDbGovernings(self, listGovernings):
        for item in listGovernings['dataCabildo']:
            try:
                governings = Governings(
                    id_governing = int(item["id_regidor"]),
                    name = unicodedata.normalize('NFKD', item["nombre_regidor"]).encode('ASCII', 'ignore'),
                    semblance = unicodedata.normalize('NFKD', item["semblanza_regidor".encode('ASCII', 'ignore')]),
                    url_photo = item["foto_regidor"],
                    status = int(item["status_regidor"]),
                    num_governing = item["numero_regidor"],
                    email = item["correo_regidor"],
                )
                base.add(governings)
                base.commit()
            except Exception as error:
                print(error)
            print("Base de datos actualizada")
            return "Base de datos actualizada", 200