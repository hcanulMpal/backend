from asyncio.windows_events import NULL
import email
from email.policy import default
from enum import unique
from unicodedata import name
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
import datetime

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    user_name = db.Column(db.String(20), unique=True, nullable=False)
    first_name = db.Column(db.String(20), nullable=True)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    mobile = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(160), nullable=False)
    is_user_active = db.Column(db.Boolean, nullable=False, default=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id', ondelete='SET NULL'), nullable=True)
    created_date = db.Column(db.DateTime, default=datetime.datetime.now)
    update_on = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())


class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    user = db.relationship(
        'User',
        uselist=False,
        backref='role',
        lazy=True
    )
    

class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    code = db.Column(db.String(32), unique=True, nullable=False)#Token Generado
    final_date = db.Column(db.Date)#Fecha en la que expeira el Token
    count_date = db.Column(db.Integer)#Contador de dias para la expiracion
    created_date = db.Column(db.DateTime, default=datetime.datetime.now)
    update_on = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())


class Officials(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False) 
    id_officials = db.Column(db.Intiger, unique=True, nullable=False) #Id del funcionario
    name = db.Column(db.String(100), nullable=False) #Nombre del funcionario
    semblance = db.Column(db.String(200), nullable=False) #Semblanza del funcionario
    url_photo = db.Column(db.String(200), unique=True, nullable=False) #Direccion url de la foto del funcionario
    dependence = db.Column(db.String(100), nullable=False) #Dependencia del funcionario
    email = db.Column(db.String(100), unique=True, nullable=False) #Direccion de contacto del funcionario
    status = db.Column(db.Boolean, nullable=False) #Si el funcionario esta activo
    created_date = db.Column(db.DateTime, default=datetime.datetime.now)
    update_on = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())


class Governings(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False) 
    id_goverming = db.Column(db.Intiger, unique=True, nullable=False) #Id del gobernante
    name = db.Column(db.String(100), nullable=False) #Nombre del gobernante
    semblance = db.Column(db.String(200), nullable=False) #Semblanza del gobernante
    url_photo = db.Column(db.String(200), unique=True, nullable=False) #Direccion url de la foto del gobernante
    status = db.Column(db.Boolean, nullable=False) #Si el gobernante esta activo o no
    num_goverming = db.Column(db.String(30), unique=True, nullable=False) #Posicion del gobernante
    email = db.Column(db.String(50), nullable=False) #Direccion de contacto del gobernante
    created_date = db.Column(db.DateTime, default=datetime.datetime.now)
    update_on = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
