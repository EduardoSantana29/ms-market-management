from flask import Flask, render_template
from flask_jwt_extended import JWTManager
from src.config.data_base import init_db, db
from src.route import init_routes
from src.route import blueprint
import os
from src.application.service.product_service import ProductService 
from src.application.controller.sale_controller import sale_bp
from flask_cors import CORS



def create_app():
    """Inicializa a aplicação Flask e a base de dados SQLite."""
    app = Flask(__name__, template_folder='src/templates', static_folder='src/static')
    CORS(app)

     # Configuração do JWT
    app.config['JWT_SECRET_KEY'] = '9f1c7d2e3b6a4e2a9f7b6c5a1a4f3c2d1e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b'  # Substitua por sua chave secreta
    app.config['JWT_TOKEN_LOCATION'] = ['headers']  # Define onde o token será procurado (cabeçalho)

    jwt = JWTManager(app)

    init_db(app)
    init_routes(app)

    with app.app_context():
        from src.infrastructure.model import product, user, sale  # adicione isso ANTES de db.create_all()
        db.create_all()
        print("📌 Tabelas criadas no PostgreSQL!")


    app.register_blueprint(blueprint)
    app.register_blueprint(sale_bp)


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

@app.route('/produtos/cadastrar')
def cadastrar_produto():
    return render_template('create_product.html') 

@app.route('/produtos')
def listar_produtos():
    return render_template('product_list.html')

@app.route('/produtos/inativar')
def deactivate_product():
    return render_template('product_deactivate.html')

@app.route('/produtos/editar', methods=['GET'])
def update_produto():
    return render_template('update_product.html')

@app.route('/produtos/excluir', methods=['GET'])
def render_delete_product():
    return render_template('delete_product.html')

@app.route('/vendas/registrar')
def mostrar_tela_vendas():
    return render_template('sell_product.html')

if __name__ == '__main__':
    app.run(debug=True)
