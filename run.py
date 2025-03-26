from flask import Flask
from src.config.data_base import init_db, db
from src.route import init_routes
import os

def create_app():
    """Inicializa a aplicação Flask e a base de dados SQLite."""
    app = Flask(__name__)
    init_db(app)
    init_routes(app)

    with app.app_context():
        if not os.path.exists("database.db"):
            db.create_all()
            print("📌 Banco de dados SQLite criado!")

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
