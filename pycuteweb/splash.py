from PySide2.QtWidgets import QSplashScreen
from PySide2.QtGui import QPixmap

class SplashScreen:

    def __init__(self, path):
        self.__path = path
        self.splash = QSplashScreen(QPixmap(path))
    
    def show(self, time=None):
        self.splash.show()
    
    def close(self, window):
        self.splash.finish(window)
