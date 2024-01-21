from flask import jsonify,request
from datetime import datetime
from werkzeug.exceptions import InternalServerError
from . import movie 
from ...Handlers.movie import getAllMoviesHandler,getAllMoviesShowsWithTheatreHandler,bookTicketsHandler

@movie.route('/all')
def getAllMovies():
    try:
        return getAllMoviesHandler()
    except Exception as e:
        print("Error: ",e)
        raise InternalServerError()


@movie.route('/<theatre_id>')
def getAllMoviesShows(theatre_id):
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    # Convert start and end dates to datetime objects
    start_datetime = datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S")
    end_datetime = datetime.strptime(end_date, "%Y-%m-%d %H:%M:%S")
    return getAllMoviesShowsWithTheatreHandler(theatre_id,start_datetime,end_datetime)

@movie.route('/book/<show_id>')
def bookTickets(show_id):
    return bookTicketsHandler(show_id)

@movie.errorhandler(500)
def internal_server_error(error = "Something Went Wrong"):
    error_message = f"Internal Server Error: {str(error)}"
    return jsonify({"error": error_message}), 500

@movie.errorhandler(400)
def bad_request_error(error):
    error_message = f"Bad Request: {str(error.description)}"
    return jsonify({"error": error_message}), 400