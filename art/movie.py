class MovieArt:
    def __init__(self):
        self.poster = ''
        self.banner = ''
        self.fanart = ''

    def __repr__(self):
        return self.poster+', '+self.banner+', '+self.fanart

    def __str__(self):
        return self.poster+', '+self.banner+', '+self.fanart