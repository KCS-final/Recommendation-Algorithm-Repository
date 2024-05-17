from flask import jsonify
from app.son import bp
from app.son.algorithm import son_algorithm

@bp.route('/api/son/hello', methods=['GET'])
def hello_son():
    return jsonify({"message": "Hello from son"})

@bp.route('/api/son/recommend', methods=['GET'])
def recommend_son():
    recommendations = son_algorithm()
    return jsonify(recommendations)
