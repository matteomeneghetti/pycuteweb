from pycuteweb import Application
import os
# sudo apt install --reinstall libxcb-xinerama0

if __name__ == '__main__':
    dirname = os.path.dirname(__file__)

    app = Application()
    app.add_splashscreen(os.path.join(dirname, "resources/esa.gif"))
    app.spawn_window("https://www.meneghetti.dev", title="My website")
    app.start()
