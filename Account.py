import persistent
import requests
from abc import ABC, abstractmethod
import ZODB, ZODB.FileStorage

import Image
import datetime

class User(persistent.Persistent):
    def __init__(self, username, password=None):
        self._username = username
        self._password = password

        self._watchedlist = MovieList()
        self._watchinglist = MovieList()
        self._willwatchlist = MovieList()
        self._reviewlist = ReviewList()
    
    def getUsername(self):
        return self._username
    
    def getPassword(self):
        return self._password
    
    def setPassword(self, password):
        self._password = password

    def setUsername(self, username, password):
        if (password == self._password):
            self._username = username
        else:
            return -1
    
    def setPassword(self, password, confirmed_password):
        if (password == confirmed_password):
            self._password = password
        else:
            return -1
    
    def getWatchedList(self):
        return self._watchedlist
    
    def getWatchingList(self):
        return self._watchinglist
    
    def getWillWatchList(self):
        return self._willwatchlist
    
    def getReviewList(self):
        return self._reviewlist
    
    def printDetails(self):
        print("Username: " + self._username + ", Password: " + self._password)

class Movie(persistent.Persistent):
    def __init__(self, title):
        self._title = title
        self._released_year = None
        self._genre = None
        self._poster_link = None
        self._image_path = None
        self._movie_id = None

        self.getMovieDetailsFromTitle()
        self._image_path = "./poster/movie" + str(self._movie_id) + ".png"
        Image.save_image_from_url(self.getPosterLink(), self._image_path)
       
    def getImagePath(self):
        return self._image_path
    
    def getTitle(self):
        return self._title
    
    def getReleasedYear(self):
        return self._released_year
    
    def getGenre(self):
        return self._genre
    
    def getPosterLink(self):
        return self._poster_link
    
    def getMovieId(self):
        return self._movie_id
    
    def getMovieDetailsFromTitle(self):
        # search for movie by title using OMDB API
        api_key = "f5c548f1"
        url = f"http://www.omdbapi.com/?apikey={api_key}&t={self._title}"
        response = requests.get(url)
        movie_data = response.json()

        # create Movie object with fetched data
        self._release_year = movie_data.get("Year")
        self._genre = movie_data.get("Genre")
        self._poster_link = movie_data.get("Poster")
        self._movie_id = movie_data.get("imdbID")

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
    
    def printDetails(self):
        print("Title: " + self._title + ", Released_year: " + self._released_year + ", Genre: " + self._genre + ", Poster_link: " + self._poster_link)

class ReviewMovie(persistent.Persistent):
    def __init__(self, movie, review_text, star_rating):
        self._movie = movie
        self._review_text = review_text
        self._star_rating = star_rating

        self._date_time = datetime.datetime.now()
    
    def getMovie(self):
        return self._movie
    
    def getReviewText(self):
        return self._review_text
    
    def getStarRating(self):
        return self._star_rating
    
    def getDateTime(self):
        return self._date_time
    
    def modifyReviewText(self, review_text):
        self._review_text = review_text
        self._date_time = datetime.datetime.now()

    def modifyStarRating(self, star_rating):
        self._star_rating = star_rating
        self._date_time = datetime.datetime.now()
    
    def printDetails(self):
        self._movie.printDetails()
        print("Review Text: " + self._review_text)
        print("Star Rating: " + str(self._star_rating))

class List(ABC, persistent.Persistent):
    @abstractmethod
    def addMovie(self, movie):
        pass

    @abstractmethod
    def deleteMovie(self, movie):
        pass


class MovieList(List, persistent.Persistent):
    def __init__(self):
        self._list = persistent.list.PersistentList()
        self._total_movie = 0
        
    def getList(self):
        return self._list
    
    def getTotalMovie(self):
        return self._total_movie
    
    def addMovie(self, movie):
        self._list.append(movie)
        self._total_movie += 1
    
    def deleteMovie(self, title):
        i = 0
        for m in self._list:
            if m.getTitle() == title:
                del self._list[i]
                self._total_movie -= 1
                print("i:" + str(i))
                i=i+1
                return i
            i = i+1
        
        return None
    
    def printDetails(self):
        for l in self._list:
            l.printDetails()

class ReviewList(List, persistent.Persistent):
    def __init__(self):
        self._list = persistent.list.PersistentList()
        self._total_movie = 0
        
    def getList(self):
        return self._list
    
    def getAverageRating(self):
        return self._average_rating

    def getTotalMovie(self):
        return self._total_movie
    
    def addMovie(self, movie):
        self._list.append(movie)
        self._total_movie += 1
    
    def deleteMovie(self, title):
        i = 0
        for m in self._list:
            if m.getMovie().getTitle() == title:
                del self._list[i]
                self._total_movie -= 1
                print("i:" + str(i))
                i=i+1
                return i
            i = i+1
        
        return None
    
    def printDetails(self):
        for l in self._list:
            l.printDetails()





    
  
