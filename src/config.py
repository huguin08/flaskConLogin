from datetime import timedelta

class Config:
    SECRET_KEY = 'B!1weNAt1T%kvhUI*S'


class ProductionConfig():
    pass
    
class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_PORT = 4200
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'Anakin102089&'
    MYSQL_DB = 'Codifin'

class TestingConfig():
    TESTING = True

config= {
    'development':DevelopmentConfig
}
