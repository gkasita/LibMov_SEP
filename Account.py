import ZODB, ZODB.FileStorage
import persistent
import requests
import transaction
    
class User(persistent.Persistent):
    def __init__(self, name, password):
        self.name = name
        self.password = password

        self.new_user = True
        self.watchedlist = MovieList()
        self.watchinglist = MovieList()
        self.willwatchlist = MovieList()
        self.reviewlist = MovieList()

class Movie(persistent.Persistent):
    def __init__(self, title):
        self.title = title
        self.release_year = None
        self.genre = None 
        self.poster_link = None

        self.getMovieDetailsFromTitle()
    
    def __str__(self):
        return "Title: " + self.title + ", Released year: " + self.release_year + ", Genre: " + self.genre + ", Poster Link: " + self.poster_link
    
    def printDetails(self):
        print(self.__str__())
        
    def getMovieDetailsFromTitle(self):
        # search for movie by title using OMDB API
        api_key = "f5c548f1"
        url = f"http://www.omdbapi.com/?apikey={api_key}&t={self.title}"
        response = requests.get(url)
        movie_data = response.json()

        # create Movie object with fetched data
        self.release_year = movie_data.get("Year")
        self.genre = movie_data.get("Genre")
        self.poster_link = movie_data.get("Poster")

    @staticmethod
    def getSuggestionFromTitle(title):
        # search for movie titles and show suggestions by keyword using OMDB API
        api_key = "f5c548f1"
        url = f"http://www.omdbapi.com/?apikey={api_key}&s={title}"
        response = requests.get(url)
        results = response.json().get('Search', [])
        # extract the titles from the search results
        titles = [r.get('Title') for r in results]
        return titles
    
    
class ReviewMovie(persistent.Persistent):
    def __init__(self, movie, review_text, star_rating):
        self.movie = movie
        self.review_text = review_text
        self.star_rating = star_rating
    
class MovieList(persistent.Persistent):
    def __init__(self):
        self.movielist = persistent.list.PersistentList()
    
    def addMovie(self, movie):
        self.movielist.append(movie)

    def deleteMovie(self, movie):
        i = 0
        for m in self.movielist:
            if m.title == movie.title:
                del self.movielist[i]
    
    def printDetails(self):
        for m in self.movielist:
            m.printDetails()
            
    
    

