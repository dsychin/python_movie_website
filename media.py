class Movie:
    """
    Class Movie takes title, poster image url, youtube trailer url, and
    storyline as input and stores it.
    """
    def __init__(self, title, poster_image_url,
                 trailer_youtube_url, storyline):
        """
        Assigns parameters to instance variables.
        
        Args:
            title (str): Title of the movie.
            poster_image_url (str): Link to the poster image of the movie.
            trailer_youtube_url (str): Link to the youtube trailer of movie.
            storyline (str): Storyline of the movie.
        """
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.storyline = storyline
