from flask import Flask

app = Flask(__name__)

@app.route("/api")
def hello():
    return "Hello World! This is a greeting from the Python API!"

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=7000)
