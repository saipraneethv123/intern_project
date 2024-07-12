from . import db
from werkzeug.security import generate_password_hash
# from flask_sqlalchemy import SQLAlchemy


#db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    mobile_no = db.Column(db.Integer, unique=True, nullable=False)
    gender = db.Column(db.String(60), nullable=False)
    # password_hash = db.Column(db.String(128), nullable=False)

 


    def __repr__(self):
        return f'<User {self.username}>'

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'mobile_no': self.mobile_no,
            'gender': self.gender
        }
