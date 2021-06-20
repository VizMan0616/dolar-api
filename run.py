from app import create_app
from flask import Flask

app = Flask(__name__)

from app.routes import api_bp
app.register_blueprint(api_bp)

if __name__ == '__main__':
    app.run()
