from flask import Flask, render_template

app = Flask(__name__)

# 반복문 + 조건문
@app.route("/fruits2")
def fruits2():
    fruits = ["무화과", "딸기", "망고", "멜론"]
    return render_template("fruits2.html", fruits=fruits)

if __name__ == "__main__":
    app.run(debug=True)
