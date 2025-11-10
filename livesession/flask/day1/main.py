from flask import Flask, render_template, request

app = Flask(__name__)

# 반복문 + 조건문
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/greet")
def greet():
    # url에서 name 값 받아오기
    name = request.args.get("name")
    return render_template("greet.html", name=name)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
