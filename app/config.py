
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:#Sai94417@localhost/flask_project'
    SQLALCHEMY_TRACK_MODIFICATIONS = False