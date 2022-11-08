from ..functions import fTocken, dbOfficials
import requests


Officials = dbOfficials()
Tocken = fTocken()


class OfficialsCtl:
    
   def getOfficials(self):
      response = requests.get("https://apicarrillo.felipecarrillopuerto.gob.mx/api/funcionarios/get_all?API_KEY_FCP=" + str(Tocken.validToken()))
      if Officials.setDbOfficials(response.json()):
         return "La base de datos fue actualizada"
      else:
         return "la base de datos presento un error"
   
   def setOfficials(self):
      return Officials.setOfficialsOrganigrama()