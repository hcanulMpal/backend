from ..functions.fAuthor import dbAuthor
import requests

Author = dbAuthor()

class AuthorCtl:
    
    def setAuthor(self):
        return Author.setAuthor()