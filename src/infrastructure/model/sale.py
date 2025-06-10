from src.config.data_base import db
from sqlalchemy import Numeric
from datetime import datetime

class Sale(db.Model):
    __tablename__ = 'sales'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    seller_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    sale_price = db.Column(Numeric(10, 2), nullable=False)
    sale_date = db.Column(db.DateTime, default=datetime.utcnow)

    product = db.relationship('Product', backref=db.backref('sales', lazy=True))
    seller = db.relationship('User', backref=db.backref('sales', lazy=True))

    def to_dict(self):
        return {
            "id": self.id,
            "product_name": self.product.name,
            "product_id": self.product_id,
            "seller_id": self.seller_id,
            "quantity": self.quantity,
            "sale_price": float(self.sale_price),  # conversão importante
            "sale_date": self.sale_date.strftime("%Y-%m-%d %H:%M:%S")  # formato legível
        }
