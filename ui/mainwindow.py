"""
    Qt Main Window for Minerva


"""
import os

from PySide import QtGui
from PySide import QtCore

from mediamanager.manager import FolderManager
from ui.ui_mainwindow import Ui_MainWindow


class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.actionScan.triggered.connect(self.load_shows)
        self.set_images()

    def load_shows(self):

#        folder_manager = FolderManager()
#        folder_manager.add_tv_folder(r"R:\Series")
#        folder_manager.add_tv_folder(r"S:\Series")
#        folder_manager.add_tv_folder(r"H:\Series")
#        folder_manager.scan_tv_folders()
#        showlist = folder_manager.tv_show_list
#        contents = ShowList(showlist)

        folder_manager = FolderManager()
        folder_manager.add_movie_folder(r"P:\Peliculas")
        folder_manager.add_movie_folder(r"R:\Peliculas")
        folder_manager.add_movie_folder(r"H:\Peliculas")
        folder_manager.scan_movie_folders()
        showlist = folder_manager.movie_list
        contents = ShowList(showlist)

        self.listView_2.setModel(contents)
        self.listView_2.clicked.connect(self.change_images)

    def set_images(self):
        os.chdir(r"C:\Users\santi.REGUEIRO\Desarrollo\Python\Minerva")
        self.bannerImage.setPixmap(QtGui.QPixmap("images/banner.jpg"))
        self.seasonBannerImage.setPixmap(QtGui.QPixmap("images/banner.jpg"))

        self.fanartImage.setPixmap(QtGui.QPixmap("images/fanart.jpg"))
        self.posterImage.setPixmap(QtGui.QPixmap("images/poster.jpg"))
        self.seasonPosterImage.setPixmap(QtGui.QPixmap("images/season01-poster.jpg"))
        self.thumbsImage.setPixmap(QtGui.QPixmap("images/thumb.jpg"))
        self.seasonThumbsImage.setPixmap(QtGui.QPixmap("images/season01-thumb.jpg"))
        self.clearLogoImage.setPixmap(QtGui.QPixmap("images/clearlogo.png"))
        self.clearArtImage.setPixmap(QtGui.QPixmap("images/clearart.png"))
        self.characterArtImage.setPixmap(QtGui.QPixmap("images/character.png"))

    def change_images(self,index):

        show = self.listView_2.model().show(index)

        folder = show.folder


        if show.art.banner:
            self.bannerImage.setPixmap(QtGui.QPixmap(show.art.banner))
        if show.art.banner:
            self.seasonBannerImage.setPixmap(QtGui.QPixmap(show.art.banner))

        if show.art.fanart:
            self.fanartImage.setPixmap(QtGui.QPixmap(show.art.fanart))
        if show.art.poster:
            self.posterImage.setPixmap(QtGui.QPixmap(show.art.poster))
        if show.art.season_poster:
            try:
                self.seasonPosterImage.setPixmap(QtGui.QPixmap(show.art.season_poster['1']))
            except KeyError:
                pass

    def resizeEvent(self, *args, **kwargs):
        self.window().setWindowTitle(str(self.size()))

class ShowList(QtCore.QAbstractListModel):
    def __init__(self, contents):
        super(ShowList, self).__init__()
        self.contents = contents

    def rowCount(self, parent):
        return len(self.contents)

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            return str(self.contents[index.row()].name)

    def show(self, index):
        return self.contents[index.row()]
