from flask import jsonify
from ..middlewares import Verify
from ..functions import functionUser


class Authorization():
    def newUser(self, data):
        if  Verify().verifyUser(data['user_name']):
            return jsonify({"data":'El usuario existe'}), 401
        
        if Verify().verifyMail(data['email']):
            return jsonify({"data":'El usuario existe'}), 401

        try:
            return functionUser().saveUser(data), 200
        except Exception as error:
            return jsonify({"error":str(error)}), 500


    def SignIn(self, data):   
        print(data['data'])                                            
        if  Verify().verifyUser(data['data']['user']):
            if  Verify().verify_password(data['data']['user'], data['data']['password']):
                return Verify().getToken(data['data']['user'])
            else:
                return jsonify({"data":'This password is incorrect'}), 401
        else:
            return jsonify({"data":'This user is incorrect'}), 401
        
    
    def getListUser(self):
            return functionUser().listUser(), 200
