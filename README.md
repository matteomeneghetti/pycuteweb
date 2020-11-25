# pycuteweb

This package aims to display webapps, websites, or other forms of HTML content on a GUI window.

It is currently built entirely on PySide2, Qt for Python.

## Example

On Debian/Ubuntu based system it is required to install some shared libraries:

```
sudo apt install --reinstall libxcb-xinerama0
```

Actual example
```python
from pycuteweb import Application
import os

app = Application()

# (Optional) Add a simple splash screen
dirname = os.path.dirname(__file__)
app.add_splashscreen(os.path.join(dirname, "resources/esa.gif"))

# Load a webpage
app.spawn_window("https://www.meneghetti.dev", title="My website")

# Render all windows and start the app
app.start()
```

## Flask example

In case you want to run a desktop application with flask, just pass the flask object
in the constructor and start the app.

```python
# Minimal example
from flask import Flask
from pycuteweb import Application

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello world!"


if __name__ == '__main__':
    web_app = Application(flask_app=app)
    web_app.start()
```


### Dependencies

- PySide2 <i>LGPLv3</i>
