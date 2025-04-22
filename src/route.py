from flask import jsonify, make_response, Blueprint
from src.application.controller.user_controller import UserController
from src.application.controller.product_controller import ProductController
from flask_jwt_extended import jwt_required, get_jwt_identity

blueprint = Blueprint('api', __name__)

def init_routes(app):
    @blueprint.route('/api', methods=['GET'])
    def health():
        """Endpoint que valida o estado da API e se a aplicação está funcionando."""
        return make_response(jsonify({"mensagem": "API - OK"}), 200)

    @blueprint.route('/api/sellers', methods=['POST'])
    def register_seller():
        """Endpoint que cadastra um vendedor na aplicação."""
        return UserController.register_seller()

    @blueprint.route('/api/sellers/activate', methods=['POST'])
    def activate_seller():
        """Endpoint que ativa o vendedor na aplicação."""
        return UserController.activate_seller()

    @blueprint.route('/api/auth/login', methods=['POST'])
    def login():
        """Endpoint que autentica o vendedor na aplicação."""
        return UserController.login()
    
      # Rotas de produtos
    @blueprint.route('/api/products', methods=['POST'])
    def create_product():
        return ProductController.create_product()

    @blueprint.route('/api/products/<int:product_id>', methods=['PUT'])
    def update_product(product_id):
        return ProductController.update_product(product_id)
    
    @blueprint.route('/api/products/<int:product_id>/deactivate', methods=['PUT'])
    @jwt_required()
    def deactivate_product(product_id):
        return ProductController.deactivate_product(product_id)

    @blueprint.route('/api/products', methods=['GET'])
    def list_products():
        return ProductController.list_products()
    
    @blueprint.route("/api/dashboard", methods=["GET"])
    @jwt_required()
    def dashboard():
        current_user = get_jwt_identity()
        return jsonify({"mensagem": f"Bem-vindo, usuário {current_user}!"})
    

'''
    @blueprint.route('/api/products/<int:product_id>', methods=['DELETE'])
    def delete_product(product_id):
        return ProductController.delete_product(product_id)
'''
