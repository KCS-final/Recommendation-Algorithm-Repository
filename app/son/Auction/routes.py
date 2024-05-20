
from flask import Blueprint, jsonify

auction_bp = Blueprint('auction', __name__)

@auction_bp.route('/')
def index():
    return jsonify({"message": "Welcome to the Auction section"})
