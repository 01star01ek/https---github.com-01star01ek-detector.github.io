# routes/ex.py
from flask import Blueprint, request, jsonify, render_template

ex_bp = Blueprint('ex', __name__)  # url_prefix 추가

@ex_bp.route('/ex')  # /ex로 접속
def ex_index():
    return render_template('ex.html')

""""
@ex_bp.route('/ex', methods=['POST'])  # POST 요청은 같은 /ex 경로로
def create_report():
    data = request.get_json()
    return jsonify({'reportId': 1, 'status': data['status']}), 201

@ex_bp.route('/ex/<int:ex_id>', methods=['GET'])  # /ex/1 같은 형식
def get_report(ex_id):
    return jsonify({
        'type': 'phone',
        'phoneNumber': '01012345678',
        'bankAccount': '1234567890',
        'isPhishing': True
    }), 200


"""