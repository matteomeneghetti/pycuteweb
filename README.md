# pycuteweb

This package aims to display webapps, websites, or other forms of HTML content on a GUI window.

It is currently built entirely on PySide2, Qt for Python.

## Example

On Debian/Ubuntu based system it is required to install some shared libraries:

```
sudo apt install --reinstall libxcb-xinerama0
```

Actual example
```
from pycuteweb import Application

app = Application()

# (Optional) Add a simple splash screen
app.addSplashScreen("./esa.gif")

# Load a webpage
app.spawn_window("https://www.meneghetti.dev")

# Render all windows and start the app
app.start()

```


### Dependencies

- PySide2 <i>LGPLv3</i>
