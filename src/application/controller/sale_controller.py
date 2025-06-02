from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.application.service.sale_service import perform_sale
from flask_cors import CORS

class SaleController:
    
    @staticmethod
    @jwt_required()
    def sell_product_api():
    data = request.get_json()
    if not data:
        return jsonify({"erro": "Corpo da requisição vazio"}), 400

    product_id = data.get('product_id')
    quantity = data.get('quantity')

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
