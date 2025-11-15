from flask import flash, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user
from models import User, users

def configure_route(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']

            user = User.get(username)

            if user in users[username]['password'] == password:
                login_user(user)

                return redirect(url_for('index'))
            else:
                flash('Invalid username or password')

        return render_template('login.html')

    @app.route('/logout')
    def logout():
        logout_user()

    @app.route('/protected')
    @login_required
    def protected():
        return "<h1>Protected area</h1> <a href='/logout>Logout</a>"
