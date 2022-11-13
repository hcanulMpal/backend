from ..functions.fPrensa import dbPrensa
import requests

Prensa = dbPrensa()


class PrensaCtl:

    def setPrensa():
        return Prensa.setPrensa()