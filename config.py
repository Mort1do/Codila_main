import os

class Config(object):
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'fsdkfd32r234fsdf'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Yellow-King8987@localhost/user_test'
    SQLALCHEMY_MODIFICATIONS = False
    SQLALCHEMY_MODIFICATIONS = False

