import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'default'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    SSL_REDIRECT = False

class DefaultConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(basedir, 'dev.db')
    DEBUG = True

config = {
    'default': DefaultConfig
}
