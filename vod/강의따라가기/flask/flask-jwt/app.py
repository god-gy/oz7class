from flask import Flask, render_template
from flask_jwt_extended import JWTManager
from routes.user import user_bp

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'jwt-secret-key'

app.register_blueprint(user_bp, url_prefix='/user')

jwt = JWTManager(app)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
