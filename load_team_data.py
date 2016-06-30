"""loaddata is a module for accessing scraped data about movies from
BoxOfficeMojo and Metacritic.
It's built specifically to work with the data collected for the
CapitalOne Metis Data Science Python Bootcamp Pilot Extravaganza 2K16.
"""

# imports
import os
import json
import pprint
import pandas as pd

# add logging info

# helper functions
def get_paths(directory):
    files = os.listdir(directory)
    return map(lambda fn : os.path.join(directory, fn), files)

def get_data(target_file_path):
    with open(target_file_path, 'r') as target_file:
        movie = json.load(target_file)
        return movie

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

class Movies(object):

    def __init__(self, directory):
        self.directory = directory

    def load_movies(self):
        paths = get_paths(self.directory)
        movies_dict = map(get_data, paths)
        return movies_dict


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
