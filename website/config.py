class Config(object):
    APP_NAME = "Foxbot Game Picker"
    STATIC_FOLDER = 'website/static'
    DEBUG = True

    DEVELOPMENT = False
    TESTING = False
    STAGING = False
    PRODUCTION = False
    # on windows:
    #SQLALCHEMY_DATABASE_URI = 'postgresql://kathrin:password@localhost:5433/gamepicker'
    # on linux:
    #SQLALCHEMY_DATABASE_URI = 'postgresql://kathrin@localhost/gamepicker'
    # on production:
    SQLALCHEMY_DATABASE_URI = 'postgresql://apps:apps@localhost/gamepicker'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEVELOPMENT = True


class TestingConfig(Config):
    TESTING = True


class StagingConfig(Config):
    STAGING = True


class ProductionConfig(Config):
    PRODUCTION = True
    DEBUG = False
