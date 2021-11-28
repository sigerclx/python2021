from datetime import timedelta
import os

config_path = os.path.abspath(os.path.dirname(__file__))


class Config:

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_EXPIRATION_DELTA = timedelta(seconds=300)
    JWT_AUTH_URL_RULE = '/auth/login'
    JWT_AUTH_HEADER_PREFIX = os.environ.get('JWT_AUTH_HEADER_PREFIX', 'FLASK')
    SECRET_KEY = os.environ.get('SECRET_KEY', 'flask123')
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///demo.db"
    JWT_AUTH_HEADER_PREFIX = 'FLASKdev'  # token 的前缀 ，FLASK+空格
    SECRET_KEY = "flask123"
    DEBUG = True


class ProductionConfig(Config):
    pass


app_config = {
    'testing': TestingConfig,
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
