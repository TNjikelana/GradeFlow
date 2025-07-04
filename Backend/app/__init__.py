from flask import Flask
from .extensions import db, login_manager, bcrypt
from .config import Config
from .routes import auth_routes, user_routes, module_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    app.register_blueprint(auth_routes)
    app.register_blueprint(user_routes)
    app.register_blueprint(module_routes)

    return app
