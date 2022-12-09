from ..functions import dbImgId_Category
import requests

ImgCate = dbImgId_Category()

class ImgCatCtl:
    
    def setId_Category(self):
        return ImgCate.setId_Category()