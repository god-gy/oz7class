from flask import Flask, render_template
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    'admin':'secret',
    'guest':'pw123'
}

@auth.verify_password   # 사용자 인증 : 사용자 이름과 비밀번호가 유효한지 확인
def verify_password(username, password):
    if username in users and users[username] == password:
        return username

@app.route('/')
def index():
    return render_template('/index.html')

@app.route('/protected')
@auth.login_required    # 라우트 보호 : 인증된 사용자만 해당 라우트로 접근할 수 있도록하는 목적
def protected():
    return render_template('/secret.html')

if __name__ == '__main__':
    app.run(debug=True)
