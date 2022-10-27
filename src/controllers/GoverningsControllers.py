from ..functions import fTocken, dbGovernings
import requests



Tocken = fTocken()
Governings = dbGovernings()


class GoverningsCtl:
    

    def getGovernings(self):
        response = requests.get("https://apicarrillo.felipecarrillopuerto.gob.mx/api/regidores/get_all?API_KEY_FCP=" + str(Tocken.validToken()))
        if Governings.setDbGovernings(response.json()):
         return "La base de datos fue actualizada"
        else:
            return "la base de datos presento un error"


    def setGoverning(self):
        return Governings.setGoverningsOrganigram()

   