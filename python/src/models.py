from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mysql import TINYINT, VARCHAR

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://mps2admin@mps2db:ParolaSecure1!@mps2db.mysql.database.azure.com/mps2projectdev2'
db = SQLAlchemy(app)


class Employee(db.Model):
    id_employee = db.Column(db.Integer, primary_key=True)
    name = db.Column(VARCHAR(30))
    surname = db.Column(VARCHAR(30))
    mail = db.Column(VARCHAR(30))
    password = db.Column(VARCHAR(30))
    is_active = db.Column(TINYINT(1))
    id_center = db.Column(db.Integer, db.ForeignKey("Transfusion_Center.id_center"))
