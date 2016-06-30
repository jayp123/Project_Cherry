"""loaddata is a module for accessing scraped data about movies from
BoxOfficeMojo and Metacritic.
It's built specifically to work with the data collected for the
CapitalOne Metis Data Science Python Bootcamp Pilot Extravaganza 2K15.
"""

# imports
import os
import json
import pprint 
import datetime
import pandas as pd

# constants
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
DATA_DIR = os.path.abspath(os.path.join(CURRENT_DIR, 'data'))

def get_movies(movie_lister):
    """This function takes a string that is the name of a
    movie_lister (which should be the name of a folder)
    and turns the movies and their attributes in that folder 
    into a pandas DataFrame"""
    
    MOJO_DIR = os.path.join(DATA_DIR, movie_lister)
    file_contents = os.listdir(MOJO_DIR)

    movie_list = []

    for filename in file_contents:
        filepath = os.path.join(MOJO_DIR, filename)

        with open(filepath, 'r') as movie_file:
            movie_data = json.load(movie_file)

        movie_list.append(movie_data)

    print "Parsed %i movies from %i files" % (len(movie_list),
                                              len(file_contents))
    return movie_list
    
def movie_date_to_datetime(date_string):
    """This function converts strings in the form of
    YYYY-MM-DD to a datetime date variable""" 
    
    year = int(date_string[0:4])
    month = int(date_string[5:7])
    day = int(date_string[8:10])
    return datetime.date(year, month, day)


if __name__ == "__main__":
    pass

def clean_data(data):
    clean_movies = []
    for movie in data:
        for key, values in movie.iteritems():
            clean_dict = {}
            if type(values) == list:
                for index,value in enumerate(values,1):
                    clean_dict["{0}_{1}".format(key,index)] = value
            else:
                clean_dict[key] = values
            clean_movies.append(clean_dict)
    return clean_movies


if __name__ == "__main__":
    # constants
    CURRENT_DIR = os.path.dirname(os.path.realpath('__file__'))
    DATA_DIR = os.path.abspath(os.path.join(CURRENT_DIR, 'data'))
    MOJO_DIR = os.path.join(DATA_DIR, 'boxofficemojo')
    META_DIR = os.path.join(DATA_DIR, 'metacritic')

    meta = Movies(META_DIR)
    mojo = Movies(MOJO_DIR)
    data1 = meta.load_movies()
    data2 = mojo.load_movies()
    clean_movies = clean_data(data1)

    mojo_df = pd.DataFrame(data2)
    meta_df = pd.DataFrame(clean_movies)
