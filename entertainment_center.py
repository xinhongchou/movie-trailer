import media
import fresh_tomatoes

# make movies
mad_max = media.Movie("Mad Max: Fury Road", 
	"https://upload.wikimedia.org/wikipedia/en/2/23/Max_Mad_Fury_Road_Newest_Poster.jpg",
	"https://www.youtube.com/watch?v=woHTUsl66BY",
	"http://www.imdb.com/title/tt1392190/")

farewell = media.Movie("Farewell My Concubine", 
	"https://upload.wikimedia.org/wikipedia/en/c/c5/Farewell_My_Concubine_poster.jpg",
	"https://www.youtube.com/watch?v=UkdFtNyvsBM",
	"http://www.imdb.com/title/tt0106332/")

samurai = media.Movie("The Seven Samurai", 
	"https://upload.wikimedia.org/wikipedia/en/8/84/Seven_Samurai_movie_poster.jpg",
	"https://www.youtube.com/watch?v=Ok3uTBZdQ6s",
	"http://www.imdb.com/title/tt0047478/")

godfather = media.Movie("The Godfather", 
	"https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg",
	"https://www.youtube.com/watch?v=5DO-nDW43Ik",
	"http://www.imdb.com/title/tt0068646")

confessions = media.Movie("Confessions", 
	"https://upload.wikimedia.org/wikipedia/en/c/cf/Confessions_%282010%29_film_poster.jpg",
	"https://www.youtube.com/watch?v=Vnws8ZymxME",
	"http://www.imdb.com/title/tt1590089")

man_woman = media.Movie("Eat Drink Man Woman", 
	"https://upload.wikimedia.org/wikipedia/en/b/b4/Eat_Drink_Man_Woman.jpg",
	"https://www.youtube.com/watch?v=yicBx-okC3k",
	"http://www.imdb.com/title/tt0111797/")

# let's the fun begin
movies = [mad_max, farewell, samurai, godfather, confessions, man_woman]
fresh_tomatoes.open_movies_page(movies)