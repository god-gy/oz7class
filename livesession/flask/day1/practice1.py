from flask import Flask # Flask 가져오기

app = Flask(__name__)   # 내가 flask를 쓸껀데 app이르는 이름을 통해서 쓸꺼임

@app.route("/") # 루트 호출시
def hello_world():
    return "Hello!"  # 루트 호출시 나오는 값

if __name__ == "__main__":  # 해당 함수를 기준으로 실행함
    app.run(debug=True)    # 서버 실행
