from flask import Blueprint, jsonify

like_bp = Blueprint('like', __name__)

@like_bp.route('/')
def index():
    return jsonify({"message": "Welcome to the Like section"})

