import os


basedir = os.path.abspath(os.path.dirname(__file__))

# uncomment the line below for postgres database url from environment variable
# postgres_local_base = os.environ['DATABASE_URL']
mysql_local_database = 'mysql+pymysql://root:@localhost:3306/madero'
sqlite_local_database_test = 'sqlite:///' + os.path.join(basedir, 'gestorclientesdb.db')


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'fThWmZq4t7w!z%C*F-JaNdRgUkXn2r5u')
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = mysql_local_database
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = mysql_local_database
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    # uncomment the line below to use postgres
    SQLALCHEMY_DATABASE_URI = mysql_local_database


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
