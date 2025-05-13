from flask import request, jsonify, make_response
from src.application.service.product_service import ProductService
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.infrastructure.model.product import Product

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
        current_user_id = get_jwt_identity()
        product = ProductService.deactivate_product(product_id, current_user_id)

        if not product:
            return make_response(jsonify({"erro": "Produto não encontrado ou não autorizado"}), 404)

        return make_response(jsonify({"mensagem": "Produto inativado com sucesso!"}), 200)


    @staticmethod
    @jwt_required()
    def get_product(product_id, user_id):
        """Método para buscar um produto específico de um vendedor"""
        product = ProductService.get_product_by_id_and_seller(product_id, user_id)
        if not product:
            return make_response(jsonify({"erro": "Produto não encontrado ou não pertence a você"}), 404)
        return make_response(jsonify(product.to_dict()), 200)

    @staticmethod
    @jwt_required()
    def delete_product(product_id):
        current_user_id = get_jwt_identity()
        deleted = ProductService.delete_product_by_seller(product_id, current_user_id)
        if not deleted:
            return jsonify({"erro": "Produto não encontrado ou não autorizado"}), 404
        return jsonify({"mensagem": "Produto excluído com sucesso!"}), 200
