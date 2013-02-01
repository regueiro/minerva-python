#!usr/bin/env python
"""
folder scanning tests

"""

import sys

from mediamanager.manager import FolderManager, LocalArtworkManager




folder_manager = FolderManager()
folder_manager.add_movie_folder(r"P:\Peliculas")
folder_manager.add_movie_folder(r"R:\Peliculas")
folder_manager.add_movie_folder(r"H:\Peliculas")
folder_manager.scan_movie_folders()
showlist = folder_manager.movie_list

art_manager = LocalArtworkManager()
for movie in showlist:
    art_manager.find_local_movie_artwork(movie)

pass