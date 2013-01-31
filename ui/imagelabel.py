from PySide.QtGui import QLabel
from PySide.QtCore import Qt

class ImageLabel(QLabel):
    def __init__(self, parent):
        super(ImageLabel, self).__init__()

    def setPixmap(self, img):
        self.image = img
        super().setPixmap(self.image.scaled(self.size(),Qt.KeepAspectRatio,Qt.SmoothTransformation))


    def resizeEvent(self, event):
         super().setPixmap(self.image.scaled(self.size(),Qt.KeepAspectRatio,Qt.SmoothTransformation))