from ..models import db, Governings
import unicodedata

base = db.session

class dbGovernings:

    def is_validate(self):
        if Governings.query.first():
            return True

    def setDbGovernings(self, listGovernings):
        for item in listGovernings['dataCabildo']:
            try:
                governings = Governings(
                    id_goverming = int(item["id_regidor"]),
                    name = str(unicodedata.normalize('NFKD', item["nombre_regidor"]).encode('ASCII', 'ignore').decode()),
                    semblance =str(unicodedata.normalize('NFKD', item["semblanza_regidor"]).encode('ASCII', 'ignore').decode()),
                    url_photo = item["foto_regidor"],
                    status = int(item["status_regidor"]),
                    num_goverming = item["numero_regidor"],
                    email = item["correo_regidor"],
                )
                base.add(governings)
                base.commit()
            except Exception as error:
                print(error)
        return True