import os
from flask import Flask
from app.extensions import db, login_manager, bcrypt
from app.routes.auth_routes import auth_routes
from app.config import DevelopmentConfig, ProductionConfig, TestingConfig
# from app.routes.module_routes import module_routes

config_map = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig
}

def create_app():
    env = os.getenv("FLASK_CONFIG", "development")
    app = Flask(__name__)
    app.config.from_object(config_map[env])
    
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    app.register_blueprint(auth_routes)
    # app.register_blueprint(module_routes)

    return app