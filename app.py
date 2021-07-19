from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from route.user_route import user_route

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://wool:qwerqwer123@localhost:3306/test_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy()
db.init_app(app)

app.register_blueprint(user_route)