# Minimal flask app from doc: https://flask.palletsprojects.com/en/stable/quickstart/
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "hello, world"