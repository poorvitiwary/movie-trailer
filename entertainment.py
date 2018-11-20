# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 01:24:50 2018

@author: Poorvi
"""

import media
import fresh_tomatoes

# media object for movie Notting Hill
notting_hill = media.Movie("notting hill",
                        "A book author meets an american actress",
                        "https://en.wikipedia.org"\
                        "/wiki/File:NottingHillRobertsGrant.jpg",
                        "https://www.youtube.com/watch?v=4RI0QvaGoiI")

# media object for movie Before We Go
before_we_go = media.Movie("before we go",
                     "A street musician meets brooke in a subway after she misses her train",
                     "https://en.wikipedia.org"\
                     "/wiki/File:Before_We_Go_Poster.jpg",
                     "https://www.youtube.com/watch?v=vNzaiGzPoUg")

# media object for movie Intersteller
intersteller = media.Movie("Intersteller",
                           "Astronaughts who go on search for new homeof humanity",
                           "https://en.wikipedia.org"\
                           "/wiki/File:Interstellar_film_poster.jpg",
                           "https://www.youtube.com/watch?v=3PsUJFEBC74")

# media object for movie Monalisa Smile
monalisa_smile = media.Movie("Monalisa Smile",
                          "Teacher persues students to chase their dreams",
                          "https://en.wikipedia.org"\
                          "/wiki/File:Monalisasmile.jpg"
                          "https://www.youtube.com/watch?v=VqexVyd_ybI")

# media object for movie midnight in paris
midnight_in_paris = media.Movie("Midnight in Paris",
                                "Storyline",
                                "http://upload.wikimedia.org"\
                                "/wikipedia/en/9/9f"\
                                "/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=atLg2wQQxvU")

# media object for movie Enigma
enigma = media.Movie("Enigma",
                           "Breaking the code of Nazis",
                           "https://en.wikipedia.org"\
                           "/wiki/File:Enigma_film.jpg",
                           "https://www.youtube.com/watch?v=5NrfiIpUd20")

# list of all movie objects
movies = [notting_hill, before_we_go, intersteller, monalisa_smile,
          midnight_in_paris, enigma]

# generates movie trailer websites with the list of movies
fresh_tomatoes.open_movies_page(movies)