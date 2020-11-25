from PySide2.QtCore import QUrl, QCoreApplication, Qt, Slot, Signal, QObject
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QApplication, QFileDialog
from PySide2.QtWebEngineWidgets import QWebEngineView
from pathlib import Path
from threading import Event, Thread

from .window import Window
from .splash import SplashScreen


class Application(QObject):

    windows = {}

    folder_dialog_spawn = Signal(str)
    window_dialog_spawn = Signal(int, str, str)

    def __init__(self, name="Default", flask_app=None):
        QObject.__init__(self)

        self.__file_dialog_event = Event()
        self.__filename_dialog = None
        self.__splash = None

        self.folder_dialog_spawn.connect(self.__on_folder_dialog)
        self.window_dialog_spawn.connect(self.__on_window)
        QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
        self.__app = QApplication([])
        self.__app.setApplicationName(name)

        if flask_app is not None:
            self.__flask_app = flask_app
            self.__flask_thread = None
            url = self.__start_flask()
            self.spawn_window(url)

    def spawn_window(self, url="", title="Default title"):
        id = len(Application.windows)
        self.window_dialog_spawn.emit(id, url, title)
        return id

    def spawn_folder_dialog(self, title="Select directory"):
        self.folder_dialog_spawn.emit(title)
        self.__file_dialog_event.wait()
        path = self.__filename_dialog
        self.__filename_dialog = None
        return Path(path) if path else None

    def add_splashscreen(self, path):
        self.__splash = SplashScreen(path)

    @Slot(int, str)
    def __on_window(self, id, url, title):
        window = Window(url=url, title=title)
        Application.windows[id] = window

    @Slot(str)
    def __on_folder_dialog(self, title):
        self.__filename_dialog = str(QFileDialog.getExistingDirectory(
            parent=None, caption=title, options=QFileDialog.ShowDirsOnly))
        self.__file_dialog_event.set()

    def start(self):
        from sys import exit

        if self.__splash is not None:
            self.__splash.show()

            if len(Application.windows) > 0:
                self.__splash.close(Application.windows[0].qtView)

        for window in Application.windows.values():
            window.start()

        return exit(self.__app.exec_())

    def __start_flask(self, port=0):

        import socket

        def run_flask(port):
            self.__flask_app.run(port=port, threaded=True)

        if port <= 1024:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('localhost', 0))
            port = sock.getsockname()[1]
            sock.close()

        self.__flask_thread = Thread(
            target=run_flask, args=(port,), daemon=True)
        self.__flask_thread.start()

        return "http://127.0.0.1:{}".format(port)
