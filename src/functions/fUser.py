from datetime import datetime
import datetime
from ..models import db, User, Role
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask import jsonify
from flask_jwt_extended import create_access_token
from flask import jsonify
from .fRoles import functionRole

base = db.session


class functionUser:

    admin = {
        "user_name": 'hcanul',
        "first_name":"Hugo Paulino",
        "last_name":"Canul Echazarreta",
        "email":"cyber.frenetic@gmail.com",
        "mobile":"(562) 114 3235",
        "password": "ha260182ha",
        "role_id": 'Administrador',
    }

    def is_Data(self):
        if not User.query.all():
            self.saveUser(self.admin)

    
    def findUserByUserName(self, user):
        isExist = User.query.filter_by(user_name = user).first()
        if isExist:
            return True
        else:
            return False

    
    def findUserNameRolByIdRole(self, id):
        locate = User.query.filter_by(role_id=id).first()
        fullname = locate.first_name + ' ' + locate.last_name
        return fullname


    def findUserByEmail(self, email):
        isExist = User.query.filter_by(email = email).first()
        if isExist:
            return True
        else:
            return False


    def create_password(self, password):
        return generate_password_hash(password)


    def findUserbyUser(self, user):
        return User.query.filter_by(user_name=user).first()


    def findUserbyId(self, id):
        return User.query.filter_by(id=id).first()


    def verify_password(self, user, password):
        return check_password_hash(self.findUserbyUser(user).password, password)


    def setToken(self, user):
        us = base.query(User, Role).filter(User.user_name == user).filter(User.role_id == Role.id).first()
        token = create_access_token(identity = {'nombre':us[0].first_name.upper() + ' ' + us[0].last_name.upper(), 'rol':us[1].name.upper(), 'id': us[0].id}, expires_delta=datetime.timedelta(minutes=480))  
        return token, 200

    
    def saveUser(self, data):
        user = User(
            user_name = data['user_name'].upper(),
            first_name = data['first_name'].upper(),
            last_name = data['last_name'].upper(),
            email = data['email'],
            mobile = data['mobile'],
            password = self.create_password(data['password']),
            is_user_active = 1,
            role_id = functionRole().findUserRole(data['role_id']),
        )
        base.add(user)
        base.commit()
        return data['user_name'].upper()
        
        
    def listUser(self):
        us = base.query(User, Role, Departamentos).filter(User.role_id == Role.id).filter(User.departamento_id == Departamentos.id).all()
        uss = []
        for item in us:
            uss.append({
                'id': item[0].id,
                'user_name': item[0].user_name,
                'first_name': item[0].first_name,
                'last_name': item[0].last_name,
                'email': item[0].email,
                'mobile': item[0].mobile,
                'role': item[1].name,
            })
        return jsonify({"data":uss})


    def findUserbyId_Name(self, id):
        name = User.query.filter_by(id=id).first().first_name + ' ' + User.query.filter_by(id=id).first().last_name
        return name


    def getCordinador(self):
        return [{'id': item.id, 'nombre':item.first_name + ' ' + item.last_name } for item in User.query.filter_by(role_id = 3).all()]
    
    
    def getPromotor(self):
        return [{'id': item.id, 'nombre':item.first_name + ' ' + item.last_name } for item in User.query.filter_by(role_id = 4).all() ]


    def getListaPromotores(self):
        return base.query(User.id).filter(User.role_id == 4).filter(User.is_user_active == True).all()


    def setMigrationUser(self, data):
        user = User(
            id = data['id'],
            user_name = data['user_name'],
            first_name = data['first_name'],
            last_name = data['last_name'],
            email = data['email'],
            mobile = data['mobile'],
            password = data['password'],
            is_user_active = data['is_user_active'],
            ciudad_id = data['ciudad_id'],
            role_id = data['role_id'],
        )
        base.add(user)
        base.commit()
        return True