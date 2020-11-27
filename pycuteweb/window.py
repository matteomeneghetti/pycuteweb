from PySide2.QtCore import QUrl
from PySide2.QtGui import QIcon, QDesktopServices
from PySide2.QtWidgets import QDesktopWidget
from PySide2.QtWebEngineWidgets import QWebEngineView, QWebEnginePage


class Window:

    def __init__(self, url, title, icon=None):

        self.__zoom = 1.0
        self.__start_url = url
        self.qtView = QWebEngineView()

        self.qtView.setWindowTitle(title)
        if icon is not None:
            self.qtView.setWindowIcon(QIcon(icon))
        self.qtView.resize(QDesktopWidget().availableGeometry(self.qtView).size() * 0.75);

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
        self.qtView.setPage(WebPage(self.__start_url, parent=self.qtView))
        self.qtView.show()

class WebPage(QWebEnginePage):

    def __init__(self, url, parent=None):
        super(WebPage, self).__init__(parent)
        self.__url = url
        self.load(QUrl(self.__url))
    
    def acceptNavigationRequest(self, qurl, navtype, mainframe):
        if self.__url in qurl.toString():  # open in QWebEngineView
            return True
        else:
            QDesktopServices.openUrl(qurl)
            return False