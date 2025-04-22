from flask import request, jsonify, make_response
from src.application.service.product_service import ProductService
from src.application.controller.user_controller import UserController
from src.infrastructure.model.user import User
from src.infrastructure.model.product import Product
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.config.data_base import db


class ProductController:

    @staticmethod
    @jwt_required()
    def create_product():
        current_user_id = get_jwt_identity()  # Seller ID
        data = request.get_json()

        name = data.get('name')
        price = data.get('price')
        quantity = data.get('quantity')
        status = data.get('status', 'Ativo')
        image_url = data.get('image_url')

        if not name or not price or not quantity:
            return make_response(jsonify({"erro": "Campos obrigatórios ausentes"}), 400)

        product = ProductService.create_product(
            current_user_id, name, price, quantity, status, image_url
        )

        return make_response(jsonify(product.to_dict()), 201)

    @staticmethod
    @jwt_required()
    def list_products():
        current_user_id = get_jwt_identity()  # Seller ID
        products = ProductService.get_products_by_seller(current_user_id)
        
        return make_response(jsonify([product.to_dict() for product in products]), 200)

    @staticmethod
    @jwt_required()
    def update_product(product_id):
        current_user_id = get_jwt_identity()  # Seller ID
        data = request.get_json()

        name = data.get('name')
        price = data.get('price')
        quantity = data.get('quantity')
        status = data.get('status')
        image_url = data.get('image_url')

        product = ProductService.update_product(
            product_id, name, price, quantity, status, image_url
        )

        if not product:
            return make_response(jsonify({"erro": "Produto não encontrado"}), 404)

        return make_response(jsonify(product.to_dict()), 200)
    
    @staticmethod
    @jwt_required()
    def deactivate_product(product_id):
        current_user_id = get_jwt_identity()  # Seller ID
        product = ProductService.get_product_by_id_and_seller(product_id, current_user_id)

        if not product:
            return make_response(jsonify({"erro": "Produto não encontrado ou não autorizado"}), 404)

        # Alterando o status para 'Inativo'
        product.status = 'Inativo'
        db.session.commit()

        return make_response(jsonify({"mensagem": "Produto inativado com sucesso!"}), 200)

    @staticmethod
    def list_products():
        try:
            # Recupera todos os produtos do banco de dados
            products = Product.query.all()

            # Converte os produtos em uma lista de dicionários
            products_data = [product.to_dict() for product in products]

            # Retorna os produtos em formato JSON
            return jsonify(products_data), 200
        except Exception as e:
            return jsonify({'erro': str(e)}), 500



'''
    @jwt_required()
    def delete_product(product_id):
        current_user_id = get_jwt_identity()  # Seller ID
        product = ProductService.delete_product(product_id)

        if not product:
            return make_response(jsonify({"erro": "Produto não encontrado"}), 404)

        return make_response(jsonify({"mensagem": "Produto excluído com sucesso!"}), 200)
'''