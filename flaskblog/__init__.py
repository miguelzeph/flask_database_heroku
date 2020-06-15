from flask import Flask
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY']='mysecretkey'
########### Data Base Config ##################
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
#OBS: Arquivo MODELS.PY vou criar as classes para o banco de dados
###############################################
bcrypt = Bcrypt(app)# Criptografia Senha
login_manager = LoginManager(app) # Login Manager



from flaskblog import routes