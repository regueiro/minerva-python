"""
Functions for media management.

"""

import os
import xml.etree.ElementTree as ET
import re
import shutil

from mediamanager.media import TvShow, Movie
from art.tvshow import TvShowArt
from art.movie import MovieArt

class FolderManager:
    """
    Manages folders and scans media.

    """

    TV_SHOW_NFO = "tvshow.nfo"
    MOVIE_NFO = "movie.nfo"

    def __init__(self):
        """
        Initialize the folder and media lists

        """

        self.tv_source_folder_list = []
        self.movie_source_folder_list = []
        self.tv_show_list = []
        self.movie_list = []

    def add_tv_folder(self, folder):
        """
        Adds a folder to the tv show folder list

        Keyword arguments:
        folder  -- the folder to add to the list

        """

        self.tv_source_folder_list.append(folder)

    def remove_tv_folder(self, folder):
        """
        Removes a folder from the tv show folder list

        Keyword arguments:
        folder  -- the folder to remove from the list

        """

        self.tv_source_folder_list.remove(folder)


    def add_movie_folder(self, folder):
        """
        Adds a folder to the movie folder list

        Keyword arguments:
        folder  -- the folder to add to the list

        """

        self.movie_source_folder_list.append(folder)


    def remove_movie_folder(self, folder):
        """
        Removes a folder from the movie folder list

        Keyword arguments:
        folder  -- the folder to remove from the list

        """

        self.movie_source_folder_list.remove(folder)

    def scan_tv_folders(self):
        """
        Scans the folder list in search of tv shows

        """

        found_folders = self._list_folders(self.tv_source_folder_list)

        current_dir = os.curdir

        for folder in found_folders:
            os.chdir(folder)

            if os.path.exists(self.TV_SHOW_NFO):
                nfo_tree = ET.parse(self.TV_SHOW_NFO)
                nfo_root = nfo_tree.getroot()
                tv_show_id = nfo_root.find('id').text
                tv_show_name = nfo_root.find('title').text

                tv_show = TvShow(tv_show_id, tv_show_name)
                tv_show.folder = folder

                self.tv_show_list.append(tv_show)

        os.chdir(current_dir)

    def scan_movie_folders(self):
        """
        Scans the folder list in search of movies

        """

        found_folders = self._list_folders(self.movie_source_folder_list)

        current_dir = os.curdir

        for folder in found_folders:
            current_dir = os.curdir
            os.chdir(folder)

            if os.path.exists(self.MOVIE_NFO):
                nfo_tree = ET.parse(self.MOVIE_NFO)
                nfo_root = nfo_tree.getroot()
                movie_id = nfo_root.find('id').text
                movie_name = nfo_root.find('title').text

                movie = Movie(movie_id, movie_name)
                movie.folder = folder

                self.movie_list.append(movie)

        os.chdir(current_dir)

    def _list_folders(self, folder_list):
        """
        Lists the folders present in a directory

        Keyword arguments:
        folder  -- the directory to search
        """

        found_folders = []

        for folder in folder_list:
            for name in os.listdir(folder):
                if os.path.isdir(os.path.join(folder, name)):
                    found_folders.append(os.path.join(folder, name))

        return found_folders


class LocalArtworkFinder:
    """
    Finds local artwork for movies and tv shows

    """

    def find_file_type(self, filename):
        """
        Returns the art type of the argument file based on its name

        Keyword arguments:
        filename    -- the name of the file to match
        """

        poster_regex = "^poster.(png|jpg)"
        banner_regex = "^banner.(png|jpg)"
        fanart_regex = "^fanart.(png|jpg)"

        season_poster_regex = "^season\d*-poster.(png|jpg)"
        season_banner_regex = "^season\d*-banner.(png|jpg)"
        season_fanart_regex = "^season\d*-fanart.(png|jpg)"

        season_all_poster_regex = "^season-all-poster.(png|jpg)"
        season_all_banner_regex = "^season-all-banner.(png|jpg)"
        season_all_fanart_regex = "^season-all-fanart.(png|jpg)"

        season_specials_poster_regex = "^season-specials-poster.(png|jpg)"
        season_specials_banner_regex = "^season-specials-banner.(png|jpg)"
        season_specials_fanart_regex = "^season-specials-fanart.(png|jpg)"

        if re.search(poster_regex, filename):
            return "poster"
        if re.search(banner_regex, filename):
            return "banner"
        if re.search(fanart_regex, filename):
            return "fanart"
        if re.search(season_poster_regex, filename):
            return "season_poster"
        if re.search(season_banner_regex, filename):
            return "season_banner"
        if re.search(season_fanart_regex, filename):
            return "season_fanart"
        if re.search(season_all_poster_regex, filename):
            return "season_all_poster"
        if re.search(season_all_banner_regex, filename):
            return "season_all_banner"
        if re.search(season_all_fanart_regex, filename):
            return "season_all_fanart"
        if re.search(season_specials_poster_regex, filename):
            return "season_specials_poster"
        if re.search(season_specials_banner_regex, filename):
            return "season_specials_banner"
        if re.search(season_specials_fanart_regex, filename):
            return "season_specials_fanart"

    def find_season(self, filename):
        """
        Returns the season number of the provided filename

        Keyword arguments:
        filename    -- the name of the file to match

        """
        season = re.search(
            'season(.*?)-(poster|banner|fanart).(png|jpg)',
            filename
        )

        if season:
            return season.group(1).lstrip('0')

    def find_local_movie_artwork(self, movie):
        """
        Scans the movie folder for artwork

        Keyword arguments:
        movie   -- the movie to scan
        """

        if os.path.exists(movie.folder):

            for file in os.listdir(movie.folder):
                type = self.find_file_type(file)

                filename = movie.folder + "\\" + file

                if type == 'poster':
                    movie.art.poster = filename
                if type == 'banner':
                    movie.art.banner = filename
                if type == 'fanart':
                    movie.art.fanart = filename


    def read_local_artwork(self, tvshow):
        """
        Scans the tv show folder for artwork

        Keyword arguments:
        tvshow  -- the tv show to scan
        """
        if os.path.exists(tvshow.folder):

            for file in os.listdir(tvshow.folder):
                type = self.find_file_type(file)

                filename = tvshow.folder + "\\" + file

                if type == 'poster':
                    tvshow.art.poster = filename
                if type == 'banner':
                    tvshow.art.banner = filename
                if type == 'fanart':
                    tvshow.art.fanart = filename

                if type == 'season_poster':
                    season_number = self.find_season(file)
                    tvshow.local_seasons.add(season_number)
                    tvshow.art.season_poster[season_number] = filename
                if type == 'season_banner':
                    season_number = self.find_season(file)
                    tvshow.local_seasons.add(season_number)
                    tvshow.art.season_banner[season_number] = filename
                if type == 'season_fanart':
                    season_number = self.find_season(file)
                    tvshow.local_seasons.add(season_number)
                    tvshow.art.season_fanart[season_number] = filename

                if type == 'season_all_poster':
                    tvshow.art.season_poster['all'] = filename
                if type == 'season_all_banner':
                    tvshow.art.season_banner['all'] = filename
                if type == 'season_all_fanart':
                    tvshow.art.season_fanart['all'] = filename

                if type == 'season_specials_poster':
                    tvshow.local_seasons.add('0')
                    tvshow.art.season_poster['specials'] = filename
                if type == 'season_specials_banner':
                    tvshow.local_seasons.add('0')
                    tvshow.art.season_banner['specials'] = filename
                if type == 'season_specials_fanart':
                    tvshow.local_seasons.add('0')
                    tvshow.art.season_fanart['specials'] = filename


    def load_shows(self, showlist):
        """
        Starts the scan for local artwork in the show list

        Keyword arguments:
        showlist    -- the list of shows to scan
        """
        for show in showlist:
            self.read_local_artwork(show)
        return showlist

class LocalArtworkSaver:
    """
    Saves artwork images

    """

    BACKUP_FOLDER = \
        r"C:\Users\santi.REGUEIRO\Desarrollo\Python\Minerva\test\backup"
    POSTER_FILENAME = 'poster'
    BANNER_FILENAME = 'banner'
    FANART_FILENAME = 'fanart'

    def set_poster(self, media, new_poster_filename):
        """
        Copies the new poster to the movie/show folder

        Stores the old poster in the backup folder indicated
        
        Keyword arguments:
        media               -- the movie or tv show to update
        new_poster_filename -- the full route to the new poster

        """

        if os.path.exists(new_poster_filename):
            if (media.art.poster):

                full_backup_name = self.BACKUP_FOLDER+'\\'+\
                                   media.name+'-poster'+\
                                   os.path.splitext(media.art.poster)[1]

                while os.path.exists(full_backup_name):
                    full_backup_name = self._add_ending_number_to_filename(full_backup_name)

                shutil.copyfile(
                    media.art.poster,
                    full_backup_name
                )


                shutil.copyfile(new_poster_filename,media.art.poster)

            else:
                shutil.copyfile(
                    new_poster_filename,
                    media.folder+
                    '\\'+
                    self.poster_FILENAME+
                    os.path.splitext(new_poster_filename)[1]
                )

    def set_banner(self, media, new_banner_filename):
        """
        Copies the new banner to the movie/show folder

        Stores the old banner in the backup folder indicated
        
        Keyword arguments:
        media               -- the movie or tv show to update
        new_banner_filename -- the full route to the new banner

        """

        if os.path.exists(new_banner_filename):
            if (media.art.banner):

                full_backup_name = self.BACKUP_FOLDER+'\\'+\
                                   media.name+'-banner'+\
                                   os.path.splitext(media.art.banner)[1]

                while os.path.exists(full_backup_name):
                    full_backup_name = self._add_ending_number_to_filename(full_backup_name)

                shutil.copyfile(
                    media.art.banner,
                    full_backup_name
                )


                shutil.copyfile(new_banner_filename,media.art.banner)

            else:
                shutil.copyfile(
                    new_banner_filename,
                    media.folder+
                    '\\'+
                    self.banner_FILENAME+
                    os.path.splitext(new_banner_filename)[1]
                )

    def set_fanart(self, media, new_fanart_filename):
        """
        Copies the new fanart to the movie/show folder

        Stores the old fanart in the backup folder indicated
        
        Keyword arguments:
        media               -- the movie or tv show to update
        new_fanart_filename -- the full route to the new fanart

        """

        if os.path.exists(new_fanart_filename):
            if (media.art.fanart):

                full_backup_name = self.BACKUP_FOLDER+'\\'+\
                                   media.name+'-fanart'+\
                                   os.path.splitext(media.art.fanart)[1]

                while os.path.exists(full_backup_name):
                    full_backup_name = self._add_ending_number_to_filename(full_backup_name)

                shutil.copyfile(
                    media.art.fanart,
                    full_backup_name
                )


                shutil.copyfile(new_fanart_filename,media.art.fanart)

            else:
                shutil.copyfile(
                    new_fanart_filename,
                    media.folder+
                        '\\'+
                        self.FANART_FILENAME+
                        os.path.splitext(new_fanart_filename)[1]
                )


    def _add_ending_number_to_filename(self,filename):
        """
        Returns the full file name with a trailing number

        If there is a trailing number already present, add 1 to it and
        return it

        Keyword arguments:
        filename    -- the file name to add a trailing number

        """

        file_name, ext = os.path.splitext(filename)

        ending_number = re.search(
            '^(.*)(poster|banner|fanart)-(.*?)'+ext,
            filename
        )

        if ending_number:
            number = ending_number.group(3)
            next_number = int(number)+1
            file_name = file_name[:-len(number)]

            lent = len(number)

            return file_name+str(next_number)+ext

        else:
            return file_name+'-1'+ext