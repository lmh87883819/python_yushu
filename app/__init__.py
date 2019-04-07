from flask import Flask
from app.models.book import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    
    register_blueprint(app)

    db.init_app(app)
    db.create_all(app=app) 
    # app.add_url_rule('/hello',view_func=hello)
    return app

def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)