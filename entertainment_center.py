# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

import media
import fresh_tomatoes

toy_story = media.Movie(
    'Toy Story',
    'https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
    'https://www.youtube.com/watch?v=KYz2wyBy3kc')

avatar = media.Movie(
    'Avatar',
    'https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg',
    'https://www.youtube.com/watch?v=5PSNL1qE6VY')

hot_rod = media.Movie(
    'Hot Rod',
    'https://upload.wikimedia.org/wikipedia/en/7/7f/Hot-rod-poster.jpg',
    'https://www.youtube.com/watch?v=DhdrA9qz79o')

forrest_gump = media.Movie(
    'Forrest Gump',
    'https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg',
    'https://www.youtube.com/watch?v=bLvqoHBptjg')

the_dark_knight = media.Movie(
    'The Dark Knight',
    'https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg',
    'https://www.youtube.com/watch?v=_PZpmTj1Q8Q')

anchorman = media.Movie(
    'Anchorman',
    'https://upload.wikimedia.org/wikipedia/en/6/64/Movie_poster_Anchorman_The_Legend_of_Ron_Burgundy.jpg',
    'https://www.youtube.com/watch?v=NJQ4qEWm9lU')

movies = [toy_story, avatar, hot_rod, forrest_gump, the_dark_knight, anchorman]
fresh_tomatoes.open_movies_page(movies)
