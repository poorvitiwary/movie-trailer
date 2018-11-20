# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 00:30:20 2018

@author: Poorvi
"""

import webbrowser


class Movie():
    """ This class provides a way to store movie related information """

    VALID_RATINGS = ["1", "2", "3", "4"]

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        """Constructor for Movie class. Initialize with movie title,
        storyline, poster image url, and trailer url """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ opens a webbrowser to show trailer """
        webbrowser.open(self.trailer_youtube_url)
