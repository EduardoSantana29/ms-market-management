from src.infrastructure.model.product import Product
from src.config.data_base import db

class ProductService:
    """Serviços relacionados a produtos para o seller"""

    @staticmethod
    def create_product(seller_id, name, price, quantity, status, image_url):
        """Cadastra um novo produto para o seller autenticado."""
        new_product = Product(
            name=name,
            price=price,
            quantity=quantity,
            status=status,
            image_url=image_url,
            seller_id=seller_id
        )
        db.session.add(new_product)
        db.session.commit()
        return new_product

    @staticmethod
    def get_products_by_seller(seller_id):
        """Retorna os produtos cadastrados pelo seller autenticado."""
        return Product.query.filter_by(seller_id=seller_id).all()

    @staticmethod
    def update_product(product_id, name, price, quantity, status, image_url):
        """Atualiza um produto existente."""
        product = Product.query.get(product_id)
        if product:
            product.name = name
            product.price = price
            product.quantity = quantity
            product.status = status
            product.image_url = image_url
            db.session.commit()
            return product
        return None

    @staticmethod
    def get_product_by_id_and_seller(product_id, seller_id):
        """Retorna um produto específico se ele pertencer ao seller autenticado."""
        return Product.query.filter_by(id=product_id, seller_id=seller_id).first()

'''
    @staticmethod
    def delete_product(product_id):
        """Exclui um produto pelo ID."""
        product = Product.query.get(product_id)
        if product:
            db.session.delete(product)
            db.session.commit()
            return product
        return None
'''