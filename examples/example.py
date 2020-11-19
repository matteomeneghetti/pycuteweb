from pycuteweb import Application
import threading
# sudo apt install --reinstall libxcb-xinerama0

if __name__ == '__main__':
    app = Application()
    def fun():
        app.spawn_folder_dialog()
    app.spawn_window("https://www.meneghetti.dev")
    #threading.Timer(2.0, fun).start()
    app.start()
