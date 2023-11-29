from flask import Flask, Blueprint
from os import environ
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize your DATABASE
db = SQLAlchemy()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get("DB_URL")
SECRET_KEY = environ.get('SECRET_KEY')
API_KEY = environ.get('API_KEY')

# Initialize a Flask App to use for the DATABASE
db.init_app(app)

migrate = Migrate(app,db)

from routes import user_route,admin_route

[app.register_blueprint(route) for route in globals().values() if isinstance(route,Blueprint)]