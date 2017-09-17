import webbrowser


class Movie():
    """ This class provide a way to store movie related information """
    def __init__(self, movie_title, movie_genres, movie_rating,
                 movie_storyline, movie_poster, movie_trailer):
        self.title = movie_title
        self.genre = movie_genres
        self.rating = movie_rating
        self.storyline = movie_storyline
        self.poster = movie_poster
        self.trailer = movie_trailer

    def show_trailer(self):
        webbrowser.open(self.trailer)
