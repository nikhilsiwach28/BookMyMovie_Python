# /bookmymovie/bookmymovie/database/movie_orm.py
from .orm import SessionLocal
from ..Model.movie import Movie
from ..Model.show import Show
from ..Model.ticket import Ticket

def getAllMoviesfromdb():
    session = SessionLocal()
    return session.query(Movie).all()

def getAllMoviesShowsWithTheatreFromDb(theatre_id,start_datetime,end_datetime):
    session = SessionLocal()
    print("getAllMoviesShowsWithTheatreFromDb")
    result =  (
        session.query(Show.date_time,Show.screen_id, Show.price,Movie.title,Movie.description, Movie.length,Movie.genre)
        .join(Show, Movie.id == Show.movie_id)
        .filter(Show.theatre_id == theatre_id)
        .filter(Show.date_time >= start_datetime, Show.date_time < end_datetime)
        .all()
    )
    return result 


def bookTicketsAndUpdateDb(user_id: int, show_id: int, number_of_tickets: int) -> bool:
    """
    Book tickets for a user for a specific show.

    Returns True if the booking is successful, False otherwise.
    """
    session = SessionLocal()

    try:
        # Begin a transaction
        with session.begin():
            # Retrieve the show and check availability
            show = session.query(Show).filter(Show.id == show_id).first()

            if show is None or show.available_seats < number_of_tickets:
                # Show not found or not enough available seats
                return False

            # Reserve seats for the user
            show.available_seats -= number_of_tickets

            # Create ticket records
            for _ in range(number_of_tickets):
                ticket = Ticket(user_id=user_id, show_id=show_id)
                session.add(ticket)

        # Commit the transaction if everything is successful
        return True

    except Exception as e:
        # Handle exceptions, log the error, and rollback the transaction
        print(f"Error during ticket booking: {str(e)}")
        session.rollback()
        return False

    finally:
        # Close the session
        session.close()
