# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 14:12:21 2016

@author: EXK747
"""

"""loaddata is a module for accessing scraped data about movies from
BoxOfficeMojo and Metacritic.
It's built specifically to work with the data collected for the
CapitalOne Metis Data Science Python Bootcamp Pilot Extravaganza 2K15.
"""

# imports
import re
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

def clean_data(data):
    clean_movies = []
    for movie in data:
        clean_dict = {}
        for key, values in movie.iteritems():
            if type(values) == list:
                for index,value in enumerate(values,1):
                    clean_dict["{0}_{1}".format(key,index)] = value
            else:
                clean_dict[key] = values
        clean_movies.append(clean_dict)
    return clean_movies

def title_cleaner(movie_dataframe,column):
    movie_dataframe = movie_dataframe.dropna(subset=[column])
    movie_dataframe['clean' + column] = pd.DataFrame(map(lambda x: \
                                    re.sub('[^a-zA-Z0-9]','',x).lower().strip(), \
                                    movie_dataframe[column]))
    return movie_dataframe


if __name__ == "__main__":
    
    boxofficemovies = get_movies('boxofficemojo')
    unclean_metamovies = get_movies('metacritic')
    
    metamovies = clean_data([movie for movie in unclean_metamovies if type(movie) != list])
    
    boxofficemovies = pd.DataFrame(boxofficemovies)
    metamovies = pd.DataFrame(metamovies)
    
    metamovies = metamovies.drop(metamovies[['genre','genre_2','genre_3','genre_4', \
                                'genre_5','genre_6','genre_7','genre_8', \
                                'genre_9','genre_10','unable to retrieve_1', \
                                'unable to retrieve_2']],axis=1).dropna()
