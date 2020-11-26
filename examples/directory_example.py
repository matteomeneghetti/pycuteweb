from pycuteweb import Application
import threading

if __name__ == '__main__':

    app = Application()

    def get_folder_path():
        path = app.spawn_folder_dialog()
        print(path, type(path))

    threading.Timer(1.0, get_folder_path).start()
    app.start()
