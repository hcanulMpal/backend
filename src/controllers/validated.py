from ..models import Governings, db, Officials
from ..functions.functionOfficials import fOfficials
from ..functions.functionGovernings import fGovernings

Official = fOfficials ()
Governing = fGovernings()
base = db.session

class valid:

    def validOfficials():
            resp = base.query(Officials).order_by(Officials.id_officials.desc()).first()
            print(resp)
            if resp is None:
                Official.getOfficials()
                Official.setDbOfficials()

            
                

    def validGovernings():
            resp = base.query(Governings).order_by(Governings.id_governing.desc()).first()
            print(resp)
            if resp is None:
                Governing.getGovernings()
                Governing.setDbGovernings()