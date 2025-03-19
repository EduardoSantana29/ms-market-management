from flask import Flask
from src.config.data_base import init_db
from src.route import init_routes

def create_app():
    app = Flask(__name__)
    init_db(app)
    init_routes(app)
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
