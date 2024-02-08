import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('postgresql://aycgzwzk:DY030ruc39hoQ9QLSD0TsCEcDdrObKOK@baasu.db.elephantsql.com/aycgzwzk') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')