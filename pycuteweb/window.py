from PySide2.QtCore import QUrl
from PySide2.QtGui import QIcon, QDesktopServices
from PySide2.QtWidgets import QDesktopWidget, QMainWindow
from PySide2.QtWebEngineWidgets import QWebEngineView, QWebEnginePage


class Window:

    def __init__(self, url, title, icon=None):

        self.__zoom = 1.0
        self.__start_url = url
        self.window = QMainWindow()
        self.__webview = QWebEngineView()
        self.window.setCentralWidget(self.__webview)

        self.window.setWindowTitle(title)
        if icon is not None:
            self.window.setWindowIcon(QIcon(icon))
        self.window.resize(QDesktopWidget().availableGeometry(self.window).size() * 0.75);

    def resize(self, width, height):
        self.window.resize(width, height)
    
    def set_zoom(self, value):
        value = float(value)
        self.__webview.setZoomFactor(self.zoom)

    def start(self):
        self.__webview.setPage(WebPage(self.__start_url, parent=self.__webview))
        self.window.show()

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