from ..functions import dbOfficials
from ..functions import dbGovernings
from .OfficialsControllers import OfficialsCtl
from .GoverningsControllers import GoverningsCtl


#TODO: Funciones
Goberning = dbGovernings()
Officials =  dbOfficials()

#TODO: Controllers
Ofi = OfficialsCtl()
Gov = GoverningsCtl()


class Valide:

    def valideTables(self):
        if not Officials.is_validate():
            Ofi.getOfficials()
        if not Goberning.is_validate():
           Gov.getGovernings()
        return True


