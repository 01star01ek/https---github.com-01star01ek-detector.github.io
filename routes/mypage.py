from flask import Blueprint, jsonify

mypage_bp = Blueprint('mypage', __name__)

@mypage_bp.route('/mypage', methods=['GET'])
def get_mypage():
    return jsonify({
        'totalReports': 5,
        'totalAmount': 100,
        'totalRefund': 0
    }), 200
