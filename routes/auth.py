# routes/auth.py
from flask import Blueprint, request, jsonify, render_template

auth_bp = Blueprint('auth', __name__)

# HTML 페이지 렌더링
@auth_bp.route('/login')  # /ex로 접속했을 때 보여줄 페이지
def login_index():
    return render_template('login.html')

""""
@auth_bp.route('/join')  # /ex로 접속했을 때 보여줄 페이지
def join_index():
    return render_template('join.html')
"""

