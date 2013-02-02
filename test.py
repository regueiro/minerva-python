#!usr/bin/env python

"""
folder scanning tests

"""

import sys

from mediamanager.manager import FolderManager, LocalArtworkFinder,\
    LocalArtworkSaver




folder_manager = FolderManager()
folder_manager.add_movie_folder(r"H:\test")
folder_manager.scan_movie_folders()
showlist = folder_manager.movie_list

art_finder = LocalArtworkFinder()
art_saver = LocalArtworkSaver()

for movie in showlist:
    art_finder.find_local_movie_artwork(movie)

for movie in showlist:
    art_saver.set_poster(movie,r"H:\Peliculas\Beasts of the Southern Wild (2012) [720p] [BluRay]\poster.jpg")
    art_saver.set_banner(movie,r"R:\Series\2 Broke Girls\banner.jpg")
    art_saver.set_fanart(movie,r"R:\Series\2 Broke Girls\fanart.jpg")

#test = art_saver._add_ending_number_to_filename("poster-2.png")

pass
