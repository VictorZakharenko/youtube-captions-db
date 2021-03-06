import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, 'con.env'))


class Config(object):
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
