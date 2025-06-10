from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.application.service.sale_service import perform_sale
from src.application.service.sale_service import list_sales_by_seller
from flask_cors import CORS
import logging

_logger = logging.getLogger(__name__)

class SaleController:

    @staticmethod
    @jwt_required()
    def sell_product_api():
        if request.method == 'OPTIONS':
            return '', 204
        
        data = request.get_json()
        print(data)

        if not data:
            return jsonify({"erro": "Corpo da requisição vazio"}), 400

        product_id = data.get('product_id')
        quantity = int(data.get('quantity'))

        if not product_id or not quantity:
            return jsonify({"erro": "Campos product_id e quantity são obrigatórios"}), 400

        try:
            seller_id = get_jwt_identity()
            sale = perform_sale(seller_id, product_id, quantity)
            return jsonify({
                "mensagem": "Venda realizada com sucesso!",
                "sale": sale.to_dict()
            }), 201
        except Exception as e:
            return jsonify({"erro": str(e)}), 400


    @staticmethod
    @jwt_required()
    def list_sales_api():
        try:
            seller_id = get_jwt_identity()
            sales = list_sales_by_seller(seller_id)
            return jsonify({"vendas": sales}), 200
        except Exception as e:
            return jsonify({"erro": str(e)}), 400