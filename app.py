from flask import Flask, render_template
from routes.auth import auth_bp
from routes.ex import ex_bp
from routes.analyze import analyze_bp
from routes.mypage import mypage_bp
from routes.check import check_bp
from routes.blue import bp_blue
    
app = Flask(__name__)
     # / (메인)
app.register_blueprint(auth_bp)          # /login, /join
app.register_blueprint(ex_bp)            # /ex
app.register_blueprint(check_bp)         # /check
app.register_blueprint(analyze_bp)       # /analyze
app.register_blueprint(mypage_bp)        # /mypage
app.register_blueprint(bp_blue)
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
