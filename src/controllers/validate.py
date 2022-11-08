from ..functions import dbOfficials, dbGovernings, fType
from .OfficialsControllers import OfficialsCtl
from .GoverningsControllers import GoverningsCtl


#TODO: Funciones
Goberning = dbGovernings()
Officials =  dbOfficials()
Tipos = fType()


#TODO: Controllers
Ofi = OfficialsCtl()
Gov = GoverningsCtl()


class Valide:

    def valideTables(self):
        if not Officials.is_validate():
            Tipos.dbauto()
            Ofi.getOfficials()
        if not Goberning.is_validate():
           Gov.getGovernings()
        
        return True


