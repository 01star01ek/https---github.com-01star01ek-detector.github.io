# routes/analyze.py
from flask import Blueprint, request, jsonify
from datetime import datetime

analyze_bp = Blueprint('analyze', __name__)

@analyze_bp.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['file']
    return jsonify({'uploadId': '123', 'status': '업로드 완료'}), 201

"""
@analyze_bp.route('/analyze/<string:analysis_id>', methods=['GET'])
def get_analysis(analysis_id):
    return jsonify({
        'analysisId': analysis_id,
        'result': {
            'probability': 0.85,
            'isPhishing': True,
            'detailText': '의심되는 음성입니다'
        },
        'createdAt': datetime.now().isoformat(),
        'audioHash': 'hash123'
    }), 200
"""