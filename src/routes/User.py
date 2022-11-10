from flask import Blueprint, current_app, request
from flask_cors import CORS
from flask_jwt_extended import JWTManager, jwt_required
from ..controllers import Authorization

jwt = JWTManager(current_app)
auth = Blueprint('auth', __name__)
cors = CORS(auth, resources={ r"/api/*":{"origins":"*"}})

autoriza = Authorization()


@auth.route("/api/autho/signin", methods=['POST'])
def signIn():
	return autoriza.SignIn(request.json)


# @auth.route("/api/autho/signup", methods=['POST'])
# @jwt_required()
# def signUp():
# 	return autoriza.newUser(request.json)


# @auth.route("/api/autho/listaUser", methods=['GET'])
# @jwt_required()
# def Lista():
#     return autoriza.getListUser()