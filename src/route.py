from flask import jsonify, make_response
from src.application.controller.user_controller import UserController

def init_routes(app):
    @app.route('/api', methods=['GET'])
    def health():
        return make_response(jsonify({"mensagem": "API - OK"}), 200)

    @app.route('/api/sellers', methods=['POST'])
    def register_seller():
        return UserController.register_seller()

    @app.route('/api/sellers/activate', methods=['POST'])
    def activate_seller():
        return UserController.activate_seller()

    @app.route('/api/auth/login', methods=['POST'])
    def login():
        return UserController.login()
