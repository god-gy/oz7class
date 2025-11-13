from flask import Flask, render_template
from flask_sock import Sock

app = Flask(__name__)
sock = Sock(app)

@app.route('/')
def index():
    return render_template("sentiment.html")

@sock.route('/ws')
def wedsocket(ws):
    while True:
        text = ws.receive()
        if text is None:
            break

        # 감정 분석

        positive = ['happy', 'good', 'love', '건영']   # 긍정단어 리스트
        nagative = ['sad', 'bad', 'angry' , '동석']   # 부정단어 리스트

        ## 긍정
        # for word in positive:
        #     if word in text:
        #         ws.send('😍 긍정')
        if any(word in text.lower() for word in positive):
            ws.send('😍 긍정')

        ## 부정
        # for word in nagative:
        #     if word in text:
        #         ws.send('😡 부정')
        if any(word in text.lower() for word in nagative):
            ws.send('😡 부정')

if __name__ == "__main__":
    app.run(debug=True)
