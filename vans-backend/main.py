from flask import Flask, json
from config import DATABASE_URI


app = Flask(__name__)

@app.route("/")
def hello():
    return f"Hello! {DATABASE_URI}"

@app.route('/list')
def list():
    return "This api will return list of components from the database."

@app.route('/add')
def list():
    return "This api will add a new component to the database."


# run the application
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8080)