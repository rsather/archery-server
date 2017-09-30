from flask import Blueprint

archers = Blueprint('archers', __name__)

@archers.route('/me')
def me():
    return "This is the default archer route", 200
