from flask import Flask
from pycuteweb import Application

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello world!"


if __name__ == '__main__':
    web_app = Application(flask_app=app)
    web_app.start()