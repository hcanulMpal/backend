from ..functions import functionRole, functionUser, funcCat, fAuth, dbNotices, dbImgCat, dbImage, dbDependence, dbTramits, dbRequirements


def verifyAndCreateData():
    
    roles = functionRole().is_Data()
    user = functionUser().is_Data()
    category = funcCat().is_Data()
    authors = fAuth().is_Data()
    notices = dbNotices().is_validate()
    imgCat = dbImgCat().is_Data()
    dep = dbDependence().is_Data()
    tra = dbTramits().is_Data()
    req = dbRequirements().id_Data()