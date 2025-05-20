from flask import Flask
from .config import Config
from .extensions import db, migrate
from app.models.project import Project

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    # login_manager.init_app(app)

    from app.routes.project_routes import project_bp as project_routes
    app.register_blueprint(project_routes, url_prefix='/projects')
   
    return app
