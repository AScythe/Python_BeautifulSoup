# find 10 movies with the keyword that you provide

import omdb
from omdb import OMDBClient
import math
from collections import Counter
# pip install omdb and Counter in cell
# !pip install omdb
# !pip install Counter

API_KEY = 'fa341c9a'
# get API key from: http://www.omdbapi.com/

# if using the module level client
omdb.set_default('apikey', API_KEY)

# must use OMDb API parameters
movies = input('Input a keyword of a movie that you like to search: ')
# search and return 10 movies that contains the keyword
m = omdb.search(movies)

# print(m)
for i in m:
    print(i)
print()

# get list of movie years
movie_year = list()

for movie in m:
    a = movie['year'].replace('–', '')
    movie_year.append(a)
# print(movie_year)
# do the counting of years
dist = Counter(movie_year)
print('date of release count:', dist)
print()

# get list of movie titles in alphabetical order
movie_title = list()

for movie in m:
    b = movie['title']
    movie_title.append(b)
print(sorted(movie_title))
