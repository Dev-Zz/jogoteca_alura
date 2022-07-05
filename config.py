import os

SECRET_KEY = 'zz-dev'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = '1643114#Ze',
        servidor = 'localhost',
        database = 'jogoteca',
        )

UPLOAD_PATH = os.path.dirname(os.path.abspath( __file__)) + '/uploads'