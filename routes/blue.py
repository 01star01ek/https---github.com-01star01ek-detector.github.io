# routes/blue.py
from flask import Blueprint, render_template

bp_blue = Blueprint('blue', __name__)

@bp_blue.route('/blue')  # 슬래시 위치 확인
def print_blue():
    return "hello Blue!"