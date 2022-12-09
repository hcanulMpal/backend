from flask import Blueprint, current_app, request,json
from flask_cors import CORS
from flask_jwt_extended import JWTManager, jwt_required
from ..controllers import Authorization
from ..controllers import listAvisos
from ..controllers import listaImages
from ..controllers import listaDependence
from ..controllers import listAutotipo
from ..controllers import listAvisos2




jwt = JWTManager(current_app)
auth = Blueprint('auth', __name__)
cors = CORS(auth, resources={ r"/api/*":{"origins":"*"}})

autoriza = Authorization()
fu = listAvisos()
li = listaImages()
lD = listaDependence()
lT = listAutotipo()
fu2 = listAvisos2()


@auth.route("/api/autho/signin", methods=['POST'])
def singIn():
	 return autoriza.SignIn(request.json)


@auth.route("/api/autho/schema", methods =['GET'])
def listA():
	return fu.listA()

@auth.route("/api/autho/Prensa", methods =['GET'])
def listA2():
	return fu2.listA2()

@auth.route("/api/autho/Image", methods =['GET'])
def listaImg():
	return li.listaImg()

@auth.route("/api/autho/dependence", methods = ['GET'])
def listD():
	return lD.listD()

@auth.route("/api/autho/autor", methods= ['GET'])
def listT():
	return lT.listaT()




	

	





# @auth.route("/api/autho/signup", methods=['POST'])
# @jwt_required()
# def signUp():
# 	return autoriza.newUser(request.json)


# @auth.route("/api/autho/listaUser", methods=['GET'])
# @jwt_required()
# def Lista():
#     return autoriza.getListUser()