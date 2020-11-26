from flask import Flask
from pycuteweb import Application

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello world!"


if __name__ == '__main__':
    web_app = Application()
    web_app.add_flask(app)
    web_app.start()