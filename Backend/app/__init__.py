from flask import Flask
from .extensions import db, login_manager, bcrypt
from .config import DevelopmentConfig  # or switch this dynamically
from .routes.auth_routes import auth_routes
# (other imports...)

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    app.register_blueprint(auth_routes)
    # (register more routes)

    @app.route('/')
    def home():
        return "Welcome to the GradeFlow Backend!"

    return app
# Initialize the app