"""
    Local database implementation for movies and tv shows


"""


__author__ = 'santi'


import sqlite3
class LocalDatabase:


    _conn = sqlite3.connect('tvshows.db')


    def create_database(self):
        """
            Creates the base database file
        """
        cur = self._conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS Movies(Id INT, Name TEXT)")