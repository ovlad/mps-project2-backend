import socket, importlib
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager, jwt_required


config = importlib.import_module("."+socket.gethostname(), package="config")

db_host = config.DATABASE_CONFIG['host']
db_name = config.DATABASE_CONFIG['dbname']
db_user = config.DATABASE_CONFIG['user']
db_password = config.DATABASE_CONFIG['password']
db_port = config.DATABASE_CONFIG['port']
db_ssl_ca = config.DATABASE_CONFIG['ssl_ca']


db_connect_string = "mysql://" + db_user + ":" + db_password + "@" + db_host + "/" + db_name + "?ssl_ca=" + db_ssl_ca

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_connect_string
app.config['SQLALCHEMY_POOL_RECYCLE'] = 100
app.config['JWT_SECRET_KEY'] = config.JWT_CONFIG['JWT_SECRET_KEY']

db = SQLAlchemy(app)
ma = Marshmallow(app)
jwt = JWTManager(app)


if __name__ == "__main__":
    from views import *
    app.run(debug=True,host='0.0.0.0',port=7000)