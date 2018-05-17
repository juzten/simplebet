from movies import format_movies_list_to_dicts, search_for_movie_by_actor


class TestMovies():

    def setup(self):
        self.movies_list = ["Ocean's Eleven", "2001",
                            "Steven Soderbergh",
                            "George Clooney, Brad Pitt, Matt Damon",
                            "Forrest Gump", "1994", "Robert Zemeckis",
                            "Robin Wright, Tom Hanks, Gary Sinise"
                            ]

        self.movies_dicts = [
            {'title': self.movies_list[0], 'year': self.movies_list[1],
             'director': self.movies_list[2], 'actors': self.movies_list[3]},
            {'title': self.movies_list[4], 'year': self.movies_list[5],
            'director': self.movies_list[6], 'actors': self.movies_list[7]}]

    def test_format_movies_list_to_dict(self):
        assert format_movies_list_to_dicts(self.movies_list) == self.movies_dicts

    def test_search_for_movie_by_actor(self):
        search_term = "Tom Hanks"
        expected_search_results = [
            {'title': self.movies_list[4], 'year': self.movies_list[5],
             'director': self.movies_list[6], 'actors': self.movies_list[7]}
        ]
        assert search_for_movie_by_actor(search_term, self.movies_dicts) == expected_search_results
