# Routes/user/user_routes.py
from . import user
from flask import request,jsonify
from werkzeug.exceptions import InternalServerError,BadRequest
from website.Handlers.user import getUserProfileHandler

@user.route('/profile/<phone>')
def userProfile(phone):
    print("came here")
    try:
        fetcheduser = getUserProfileHandler(phone)
    except Exception as e:
        print("Error: ", e)
        raise InternalServerError("Something went wrong")
    
    if fetcheduser is None:
        raise BadRequest(description="User Not Found")

    return fetcheduser



@user.errorhandler(500)
def internal_server_error(error):
    error_message = f"Internal Server Error: {str(error)}"
    return jsonify({"error": error_message}), 500

@user.errorhandler(400)
def bad_request_error(error):
    error_message = f"Bad Request: {str(error.description)}"
    return jsonify({"error": error_message}), 400