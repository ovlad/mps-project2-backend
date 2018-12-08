from flask import Flask
from database import init_db

app = Flask(__name__)

@app.route("/")
def hello():
    tables = init_db()
    output = ""
    for entry in tables:
        output += entry + " "
    return output
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=7000)