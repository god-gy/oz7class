from flask import Flask, request, Response
# import test

app = Flask(__name__)

# http://127.0.0.1:5000

@app.route('/')
def home():
    return "Hello, This is Main Page!"

@app.route('/about')
def about():
    return "Hello, This is about Page!"

# 동적으로 URL 파라미터 값을 받아서 처리해준다.
# http://127.0.0.1:5000/user/godGY
@app.route('/user/<username>')
def user_profile(username):
    return f'UserName : {username}'

@app.route('/user/<int:number>')
def number(number):
    return f'number : {number}'

# post 요청 날리는 법
# 1. postman
# 2. requests

import requests

@app.route('/test')
def test():
    url = 'http://127.0.0.1:5000/submit'
    data = 'test data'
    response = requests.post(url=url, data=data)
    return response

@app.route('/submit', methods=['GET', 'POST', 'PUT', 'DELETE'])
def submit():
    print(request.method)

    if request.method == 'GET':
        print("GET method")
    if request.method == 'POST':
        print("****POST method*****", request.data)

    return Response("Success")

if __name__ == "__main__":
    print("__name__: ", __name__)
    # app.run()
    # app.run(debug=True)
