from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    """Inicializa a base de dados PostgreSQL com o app Flask e o SQLAlchemy."""
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:132607@localhost:5432/msmarket'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)