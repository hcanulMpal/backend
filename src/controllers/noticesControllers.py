from ..functions.functionNotices import dbNotices
import requests


Notis = dbNotices()


class NoticesCtl:

    def setNotices(self):
        return Notis.setNotices()