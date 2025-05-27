from src.infrastructure.model.product import Product
from src.infrastructure.model.user import User
from src.infrastructure.model.sale import Sale
from src.config.data_base import db
from flask import abort

def perform_sale(seller_id, product_id, quantity):
    product = Product.query.filter_by(id=product_id).first()
    seller = User.query.filter_by(id=seller_id).first()

    if not product:
        abort(404, description="Produto não encontrado.")
    if product.seller_id != seller_id:
        abort(403, description="Você só pode vender seus próprios produtos.")
    if product.status.lower() != "ativo":
        abort(400, description="Produto inativo.")
    if seller.status.lower() != "ativo":
        abort(400, description="Usuário inativo.")
    if quantity > product.quantity:
        abort(400, description="Estoque insuficiente.")

    # Criar venda
    sale = Sale(
        product_id=product.id,
        seller_id=seller.id,
        quantity=quantity,
        sale_price=product.price
    )
    db.session.add(sale)

    # Atualizar estoque
    product.quantity -= quantity

    db.session.commit()
    return sale
