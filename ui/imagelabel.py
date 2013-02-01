from PySide.QtGui import QLabel
from PySide.QtCore import Qt

class ImageLabel(QLabel):
    def __init__(self, parent):
        super(ImageLabel, self).__init__()
        self.image = None

    def setPixmap(self, img):
        if img:
            self.image = img
            super().setPixmap(self.image.scaled(self.size(),Qt.KeepAspectRatio,Qt.SmoothTransformation))
        else:
            self.image = None
            super().setPixmap(None)


    def resizeEvent(self, event):
        if self.image:
            super().setPixmap(self.image.scaled(self.size(),Qt.KeepAspectRatio,Qt.SmoothTransformation))