from ..functions import functionUser, functionRole 


class Verify(object):

    def verifyUser(self, user):
        return functionUser().findUserByUserName(user)

    def verifyMail(self, email):
        return functionUser().findUserByEmail(email)

    def verifyRole(self, role):
        return functionRole().findUserRole(role)

    def verify_password(self, user, password):
        return functionUser().verify_password(user, password)

    def getToken(self, user):
        return functionUser().setToken(user)
