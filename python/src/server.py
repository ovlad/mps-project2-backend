from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import models
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://mps2admin:ParolaSecure1!@mps2db.mysql.database.azure.com/mps2projectdev2'
db = SQLAlchemy(app)

@app.route("/")
def hello():
    db.create_all()
    return "Hello World! This is a greeting from the Python API!"

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=7000)
