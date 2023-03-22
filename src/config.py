from datetime import timedelta


class ProductionConfig():
    pass
    
class DevelopmentConfig():
    DEBUG = True

class TestingConfig():
    TESTING = True

config= {
    'development':DevelopmentConfig
}
