'''
    Flask와 Flask-Smorest에서 abort 함수는 요청 처리 중에 오류가 발생했을 때 사용됩니다.
    이 함수를 호출하면 특정 HTTP 상태 코드와 함께 응답이 클라이언트로 전송되며,
    선택적으로 오류 메시지나 추가 정보를 포함시킬 수 있습니다.
'''
from flask import Flask, abort

app = Flask(__name__)

@app.route('/example')
def example():
    # 어떠한 조건에서 오류를 발생시키고 처리
    error_condition = True

    if error_condition:
        abort(500, description="An error occurred while processing the request.")

    # 정상적인 응답
    return "Success!"

if __name__ == "__main__":
    app.run(debug=True)
