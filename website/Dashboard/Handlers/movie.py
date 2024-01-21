from flask import Response,jsonify
from ..Database.movie import getAllMoviesfromdb,getAllMoviesShowsWithTheatreFromDb,bookTicketsAndUpdateDb

def getAllMoviesHandler():
    fetchedMovies = getAllMoviesfromdb()
    movies =[]
    for fetchedMovie in fetchedMovies:
        movie = {
            "title" : fetchedMovie.title,
            "description" : fetchedMovie.description,
            "length" : fetchedMovie.length,
            "genre" : fetchedMovie.genre
        }
        movies.append(movie)
    return jsonify(movies)

def getAllMoviesShowsWithTheatreHandler(theatre_id,start_datetime,end_datetime):
    print("getAllMoviesShowsWithTheatreHandler")
    fetchedmovieShows = getAllMoviesShowsWithTheatreFromDb(theatre_id , start_datetime, end_datetime)
    movieShows = []
    for fetchedMovieShow in fetchedmovieShows:
        movieShow = {
                "datetime" : fetchedMovieShow.date_time,
                "screen_id" : fetchedMovieShow.screen_id,
                "price" : fetchedMovieShow.price,
                "title" : fetchedMovieShow.title,
                "description" : fetchedMovieShow.description,
                "length" : fetchedMovieShow.length,
                "genre" : fetchedMovieShow.genre
        }
        movieShows.append(movieShow)
    return jsonify(movieShows); 
    

def bookTicketsHandler(show_id):
    if show_id is None:
        return Response("Invalid Show Chosen",400)
    return bookTicketsAndUpdateDb(show_id)

