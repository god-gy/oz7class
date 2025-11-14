''' API '''
from flask import jsonify, Blueprint, request
from app.models import Review, SessionLcal


review_bp = Blueprint("review", __name__)

@review_bp.route('/reviews', methods=['GET'])
def get_reviews():
    '''전체 목록 조회'''
    db = SessionLcal()
    reviews = db.query(Review).all
    db.close()

    return jsonify([{'id': r.id, 'content': r.content} for r in reviews])

@review_bp.route('/reviews/<int:review_id>', methods=['GET'])
def get_review(review_id):
    '''특정 목록 조회'''
    db = SessionLcal()
    review = db.query(Review).get(review_id)
    db.close()
    if not review:
        return jsonify({"error": "없는 리뷰입니다."}), 404
    return jsonify({review_id: review})

# 새 리뷰 추가
@review_bp.route('/reviews', methods=['POST'])
def create_review():
    review = request.get_json()

    db = SessionLcal()
