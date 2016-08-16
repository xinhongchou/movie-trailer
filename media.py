class Movie():
    """ The Movie class to package all the movie related infomation.
        Attribute:
                  title: the title of the movie
                  poster_image_url: poster image url
                  trailer_youtube_url: the youtube link of the movie trailer
                  imdb_link: the link in IMDB database
    """
    def __init__(self, movie_title, poster_image, trailer_youtube, imdb_link):
		self.title = movie_title
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.imdb_link = imdb_link
