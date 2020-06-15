from flask import Flask
from flask_login import LoginManager
import os

app = Flask(__name__)
app.config['SECRET_KEY']=os.environ.get("SECRET_KEY") # Está no HEROKU
########### Data Base Config ##################
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app.config['SQLALCHEMY_DATABASE_URI'] =os.environ.get("DATABASE_URL") # Foi criado pelo HEROKU
#app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///database.db' #LOCAL
db = SQLAlchemy(app)
#OBS: Arquivo MODELS.PY vou criar as classes para o banco de dados
###############################################
bcrypt = Bcrypt(app)# Criptografia Senha
login_manager = LoginManager(app) # Login Manager
login_manager.login_view='login'# nome VIEW FUNCTION
login_manager.login_message_category='info' #Bootstrap, ex: alert, success...



from flaskblog import routes