from datetime import timedelta
class Config():
    #SQLALCHEMY_DATABASE_URI=  "sqlite:///demo.db"
    # 连接本地的mysql数据库，自动按model里的user 和 demo 类生成数据库的表 flask db upgrade
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/demo'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #SECRET_KEY = "flask123"
    JWT_EXPIRATION_DELTA = timedelta(seconds=300)
    JWT_AUTH_URL_RULE = '/auth/login'
    #JWT_AUTH_HEADER_PREFIX = 'FLASK'  # token 的前缀 ，FLASK+空格

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///demo.db"
    JWT_AUTH_HEADER_PREFIX = 'FLASK'  # token 的前缀 ，FLASK+空格
    SECRET_KEY = "flask123"

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///demo.db"
    JWT_AUTH_HEADER_PREFIX = 'FLASKdev'  # token 的前缀 ，FLASK+空格
    SECRET_KEY = "flask123"

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///demo.db"
    JWT_AUTH_HEADER_PREFIX = 'FLASK'  # token 的前缀 ，FLASK+空格
    SECRET_KEY = "flask123"

app_config ={
    'testing':TestingConfig,
    'development':DevelopmentConfig,
    'production':ProductionConfig
}
