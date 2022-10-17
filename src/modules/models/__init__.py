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