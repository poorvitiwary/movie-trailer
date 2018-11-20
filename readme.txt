###Project Overview

I have writen server-side code to store a list of my favorite movies, including box art imagery and a movie trailer URL. 
I have then used my code to generate a static web page allowing visitors to browse their movies and watch the trailers.


###How will I complete this project?
This project is connected to the Programming Foundations with Python course. Here's what I have done:

Installed Python
Created a data structure (i.e. a Python Class) to store my favorite movies, including movie title, box art URL (or poster URL) and a YouTube link to the movie trailer.
Created multiple instances of that Python Class to represent my favorite movies; grouped all the instances together in a list.
To generate a website that displays these movies, I have provided a starter code repository that contains a Python module called fresh_tomatoes.py.
The fresh_tomatoes.py module has a function called open_movies_page that takes in one argument, which is a list of movies, and creates an HTML file which will display all of your favorite movies.
I have ensured my website renders correctly when I attempt to load it in a browser.


###Notes

The file fresh_tomatoes.py contains the open_movies_page() function that has taken in my list of movies and generated an HTML file including this content, producing a website to showcase my favorite movies.
My task was to write a movie class in media.py. To do this, I have considered movie titles, box art, poster images, and movie trailer URLs. 
Look at what open_movies_page() does with a list of movie objects for hints on how to design your movie class.
I have writen a constructor for the movie class so that I can create instances of movie. I  hvae then created a list of these movie objects in entertainment_center.py by calling the constructor media.Movie() to instantiate movie objects.
I’ve given movies their own custom data structure by defining the movie class and constructor, and now these objects stored in a list data structure. 
This list of movies is what the open_movies_page() function takes as input in order to build the HTML file, so that I can display my website.