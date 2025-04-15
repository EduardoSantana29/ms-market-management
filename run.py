from flask import Flask, render_template
from src.config.data_base import init_db, db
from src.route import init_routes
from src.route import blueprint
import os

def create_app():
    """Inicializa a aplicação Flask e a base de dados SQLite."""
    app = Flask(__name__, template_folder='src/templates', static_folder='src/static')

    app.config['SECRET_KEY'] = '9f1c7d2e3b6a4e2a9f7b6c5a1a4f3c2d1e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b'

    init_db(app)
    init_routes(app)

    with app.app_context():
        db.create_all()
        print("📌 Tabelas criadas no PostgreSQL!")


    app.register_blueprint(blueprint)

    return app

app = create_app()

@app.route('/')
def index():
    return render_template('index.html', output="")

@app.route('/activate')
def activate():
    return render_template('activate.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route("/home")
def home():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True)
