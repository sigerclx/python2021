#https://www.cnblogs.com/-wenli/p/13949636.html
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
# private.env 作为配置文件，可以不上传github上去。后面os.environ.get就是从private.env取预设配置值
load_dotenv(os.path.join(basedir, 'private.env'))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTS_PER_PAGE = 5 # 分页，每页的记录数