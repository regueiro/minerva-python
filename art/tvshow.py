import pprint

class TvShowArt:
    def __init__(self):
        self.poster = ''
        self.banner = ''
        self.fanart = ''
        self.season_poster = {}
        self.season_banner = {}
        self.season_fanart = {}

    def __repr__(self):
        pp = pprint.PrettyPrinter()
        return self.poster+', '+self.banner+', '+self.fanart+', '+pp.pformat(self.season_poster)+', '+pp.pformat(self.season_banner)+', '+pp.pformat(self.season_fanart)

    def __str__(self):
        pp = pprint.PrettyPrinter()
        return self.poster+', '+self.banner+', '+self.fanart+', '+pp.pformat(self.season_poster)+', '+pp.pformat(self.season_banner)+', '+pp.pformat(self.season_fanart)