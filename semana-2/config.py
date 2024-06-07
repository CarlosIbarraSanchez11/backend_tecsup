import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost/codigo_18_backend'
    SQLALCHEMY_TRACK_MODIFICATIONS = True