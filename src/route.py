from flask import jsonify, make_response
from src.application.controller.user_controller import UserController

def init_routes(app):
    @app.route('/api', methods=['GET'])
    def health():
        """Endpoint que valida o estado da API e se a aplicação está funcionando."""
        return make_response(jsonify({"mensagem": "API - OK"}), 200)

    @app.route('/api/sellers', methods=['POST'])
    def register_seller():
        """Endpoint que cadastra um vendedor na aplicação."""
        return UserController.register_seller()

    @app.route('/api/sellers/activate', methods=['POST'])
    def activate_seller():
        """Endpoint que ativa o vendedor na aplicação."""
        return UserController.activate_seller()

    @app.route('/api/auth/login', methods=['POST'])
    def login():
        """Endpoint que autentica o vendedor na aplicação."""
        return UserController.login()
