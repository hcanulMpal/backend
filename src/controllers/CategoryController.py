from ..functions.fCategory import dbCategory
import requests

Category = dbCategory()

class CategoryCtl:
    
    def setCategory(self):
        return Category.setCategory()