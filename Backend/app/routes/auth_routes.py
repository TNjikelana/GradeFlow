from flask import Blueprint, request, jsonify

auth_routes = Blueprint('auth', __name__, url_prefix='/api/auth')

@auth_routes.route('/login', methods=['POST'])
def login():
    # validate user
    return jsonify({"message": "Login endpoint"})
