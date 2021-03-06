from flask import g
from flask_httpauth import HTTPBasicAuth
from app.blueprints.authentication.models import User
from .errors import error_response

basic_auth = HTTPBasicAuth()

@basic_auth.verify_password
def verify_password(email, password):
    user = User.query.filter_by(email=email).first()
    if user is None:
        return False
    g.current_user = user
    return user.check_password(password)

@basic_auth.error_handler
def basic_auth_error():
    return error_response(401)