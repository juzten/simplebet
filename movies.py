#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def main():
    """ allows a user to search a list of movies by an actor/actress name.
        Given the name of the star the user is looking for, the tool should
        print out the movies that person starred in, in order of release date
    """
    filename = 'movies.txt'
    try:
        search_term = sys.argv[1]
    except Exception as e:
        print('What gives??? You did not enter a search term')
        return

    movies_data = get_movies_list_from_file(filename)
    found_movies = search_for_movie_by_actor(search_term, movies_data)
    if found_movies:
        output_search_results(found_movies, search_term)
    else:
        print("No movies found starring '{}'".format(search_term))


def get_movies_list_from_file(filename):
    """Read txt file into list of movies."""
    movies_file_line_list = []
    with open(filename, 'r') as f:
        for line in f:
            if line != '\n':
                movies_file_line_list.append(line)

    if len(movies_file_line_list) % 4 != 0:
        print('The movie file list is messed up!')
        return
    return format_movies_list_to_dicts(movies_file_line_list)


def format_movies_list_to_dicts(movies_file_line_list):
    """Convert movies list to usable and structured dict."""
    movies = []
    beginning, end = 0, 4
    while True:
        movie_data = movies_file_line_list[beginning:end]
        movies.append({
            'title': movie_data[0].strip('\n'),
            'year': movie_data[1].strip('\n'),
            'director': movie_data[2].strip('\n'),
            'actors': movie_data[3].strip('\n')
        })

        if end < len(movies_file_line_list):
            beginning += 4
            end += 4
        else:
            break

    return movies


def output_search_results(found_movies, search_term):
    """ Output should be similar to the following if multiple results are found:

    2 Movies Featuring Tom Hanks

    Title: Forrest Gump (1994)
    Directed By: Robert Zemeckis
    Also Starring: Robin Wright, Gary Sinise

    Title: Saving Private Ryan (1998)
    Directed By: Steven Spielberg
    Also Starring: Matt Damon, Tom Sizemore
    """

    print("{} Movies Featuring {}\n".format(len(found_movies), search_term))
    for movie in found_movies:
        actors = movie['actors'].split(',')
        starring = []
        for actor in actors:
            if search_term.lower() not in actor.lower():
                starring.append(actor)
        print("Title: {} ({})".format(movie['title'], movie['year']))
        print("Directed By: {}".format(movie['director']))
        print("Also Starring: {}\n".format(",".join(starring)))


def search_for_movie_by_actor(search_term, movies_data):
    """Search for an actor in the list of movie dictionaries."""
    movies = [movie for movie in movies_data if search_term.lower() in movie['actors'].lower()]
    return movies


if __name__ == "__main__":
    main()
