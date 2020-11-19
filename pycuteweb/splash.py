from PySide2.QtWidgets import QSplashScreen
from PySide2.QtGui import QPixmap, QMovie, QPainter

class SplashScreen:

    def __init__(self, path):
        self.__path = str(path)

        supported_formats = (format.data().decode() for format in QMovie.supportedFormats())
        if self.__path.lower().endswith(tuple(supported_formats)):
            self.splash = AnimatedSplash(path)
        else:
            self.splash = ImageSplash(path)

    def show(self, time=None):
        self.splash.show()
    
    def close(self, window):
        self.splash.finish(window)


class ImageSplash(QSplashScreen):

    def __init__(self, path):
        self.__pixmap = QPixmap(path)
        QSplashScreen.__init__(self, self.__pixmap)


class AnimatedSplash(QSplashScreen):

    def __init__(self, path):

        self.__movie = QMovie(path)
        self.__movie.jumpToFrame(0)

        pixmap = QPixmap(self.__movie.frameRect().size())
        QSplashScreen.__init__(self, pixmap)
        self.__movie.frameChanged.connect(self.repaint)

    def showEvent(self, event):
        self.__movie.start()

    def hideEvent(self, event):
        self.__movie.stop()

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = self.__movie.currentPixmap()
        self.setMask(pixmap.mask())
        painter.drawPixmap(0, 0, pixmap)
