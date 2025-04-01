from flask import Flask, render_template
from src.config.data_base import init_db, db
from src.route import init_routes
from src.route import blueprint
import os

def create_app():
    """Inicializa a aplicação Flask e a base de dados SQLite."""
    app = Flask(__name__, template_folder='src/templates', static_folder='src/static')
    init_db(app)
    init_routes(app)

    with app.app_context():
        if not os.path.exists("database.db"):
            db.create_all()
            print("📌 Banco de dados SQLite criado!")

    app.register_blueprint(blueprint, url_prefix='/api')

    return app

app = create_app()

@app.route('/')
def index():
    return render_template('index.html', output="")

if __name__ == '__main__':
    app.run(debug=True)
