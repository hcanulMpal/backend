from ..functions import functionRole, functionUser


def verifyAndCreateData():
    roles = functionRole().is_Data()
    user = functionUser().is_Data()
    
