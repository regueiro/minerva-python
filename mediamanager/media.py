"""
Classes for storing media information

"""

from art import tvshow

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
        self.art = tvshow.TvShowArt()

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

    def __repr__(self):
        return self.name +': '+self.id

    def __str__(self):
        return self.name +': '+self.id