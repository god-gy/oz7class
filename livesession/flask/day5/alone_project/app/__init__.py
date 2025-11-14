''' Flask 앱 생성  '''

from flask import Flask
from .routes.review_route import review_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(review_bp)
    return app
