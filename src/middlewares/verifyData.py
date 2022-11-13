from ..functions import functionRole, functionUser
from ..functions.fCategory import funcCat
from ..functions.fAuthor import fAuth
from ..functions.functionNotices import dbNotices


def verifyAndCreateData():
    
    roles = functionRole().is_Data()
    user = functionUser().is_Data()
    category = funcCat().is_Data()
    authors = fAuth().is_Data()
    notices = dbNotices().is_validate()