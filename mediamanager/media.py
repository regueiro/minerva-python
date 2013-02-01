"""
Classes for storing media information

"""

from art.tvshow import TvShowArt
from art.movie import MovieArt

class TvShow:
    """
    Defines a tv show

    """

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.folder = ''
        self.tvdb_seasons = set()
        self.local_seasons = set()
        self.art = TvShowArt()

    def __repr__(self):
        return self.name +': '+self.id+'  '+self.art.__repr__()

    def __str__(self):
        return self.name +': '+self.id+'  '+self.art.__repr__()


class Movie:
    """
    Defines a movie

    """

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.folder = ''
        self.art = MovieArt()

    def __repr__(self):
        return self.name +': '+self.id

    def __str__(self):
        return self.name +': '+self.id