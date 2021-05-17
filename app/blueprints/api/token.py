from flask import jsonify, g
from app import db
from .import bp as api
from .auth import basic_auth

@api.route('/token', methods=['POST'])
@basic_auth.login_required
def get_token():
    token = g.current_user.get_token()
    db.session.commit()
    return jsonify({'token': token})