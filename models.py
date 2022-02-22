from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class ProductModel(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer(), unique=True)
    name = db.Column(db.String(80))
    url = db.Column(db.String(80))
    price = db.Column(db.Integer())
    amount = db.Column(db.Integer())
    comment = db.Column(db.String(80))

    def __init__(self, product_id, name, url, price, amount, comment):
        self.product_id = product_id
        self.name = name
        self.url = url
        self.price = price
        self.amount = amount
        self.comment = comment

    def __repr__(self):
        return f"{self.name}"
