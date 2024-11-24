from flask import Blueprint, request, jsonify

check_bp = Blueprint('check', __name__)

# HTML 페이지 렌더링
@check_bp.route('/check')  # /ex로 접속했을 때 보여줄 페이지
def show_report_page():
    return render_template('check.html')


@check_bp.route('/check', methods=['POST'])
def check():
    data = request.get_json()
    return jsonify({'searchId': 1, 'status': '조회 완료'}), 201

@check_bp.route('/check_t', methods=['GET'])
def get_check_result():
    return jsonify({
        'searchId': 1,
        'bankCode': '신한',
        'accountNumber': '1234567890',
        'phoneNumber': '01012345678',
        'isPhishing': False,
        'searchDate': datetime.now().isoformat()
    }), 200