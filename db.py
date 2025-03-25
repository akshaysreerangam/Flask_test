from flask import Flask

from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

db=SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

db.init_app(app)