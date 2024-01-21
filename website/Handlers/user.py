from website.Database.user import getUserFromDb
from flask import jsonify

def getUserProfileHandler(phone):
    user = getUserFromDb(phone)
    user_data = {
        "name": user.name,
        "email": user.email,
        "phone": user.phone
    }
    return jsonify(user_data)