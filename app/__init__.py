from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
#from .common import Config

#api_db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
#    app.config.from_object(Config)

#    api_db.init_app(app)

    from .routes import api_bp
    app.register_blueprint(api_bp)

    return app

