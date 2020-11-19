from PySide2.QtCore import QUrl
from PySide2.QtGui import QIcon
from PySide2.QtWebEngineWidgets import QWebEngineView


class Window:

    def __init__(self, title="Default title", icon=None, url=""):

        self.__zoom = 1.0
        self.__url = url
        self.qtView = QWebEngineView()

        self.qtView.setWindowTitle(title)
        if icon is not None:
            self.qtView.setWindowIcon(QIcon(icon))

    def resize(self, width, height):
        self.qtView.resize(width, height)

    @property
    def zoom(self):
        return self.__zoom

    @zoom.setter
    def zoom(self, value):
        value = float(value)
        self.__zoom = value
        self.qtView.setZoomFactor(self.zoom)

    def start(self):
        self.qtView.setUrl(QUrl(self.__url))
        self.qtView.show()
