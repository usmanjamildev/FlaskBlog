import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fd8f9b8ffe0306f346cdc5ef2f87d140'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'usmanjamil876@gmail.com'
<<<<<<< HEAD
app.config['MAIL_PASSWORD'] = 'jbfo cfvy fxvb tvwa'
=======
app.config['MAIL_PASSWORD'] = 'rcto iefq kils xclk'
>>>>>>> 2d9e6b4dcdbcce26c54209632eac69b4627f0b16
app.config['MAIL_DEFAULT_SENDER'] = 'usmanjamil876@gmail.com'

mail = Mail(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
from flaskblog import routes
