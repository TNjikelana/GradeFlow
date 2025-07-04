from flask import Flask
from .config import Config
from .extensions import bcrypt, db, login_manager
from .routes import auth_routes, module_routes, user_routes

import os

def create_app(config_class=None):
    """
    Application factory function for creating and configuring the Flask app.
    Allows parameterization of the configuration for different environments.
    """
    app = Flask(__name__)
    if config_class is None:
        config_name = os.environ.get('FLASK_CONFIG', 'Config')
        from . import config as config_module

    # Register blueprints in the following order to avoid route conflicts.
    # If any blueprints have overlapping routes, update this order and test accordingly.
    
    app.config.from_object(Config)
    app.register_blueprint(auth_routes)
    app.register_blueprint(user_routes)
    app.register_blueprint(module_routes)
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    app.register_blueprint(auth_routes)
    app.register_blueprint(user_routes)
    app.register_blueprint(module_routes)

    return app
