class Config(object):
    SECRET_KEY = 'sam' 
    # SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL')
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:alanna94@localhost/wildlife"
    SQLALCHEMY_TRACK_MODIFICATIONS = False