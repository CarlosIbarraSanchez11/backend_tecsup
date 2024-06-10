from flask import Blueprint, jsonify, request
from extensions import db
from entities.product_model import Product

products_bp = Blueprint('products', __name__)

# GET Todos los productos
@products_bp.route('/api/v1/product')
def get_all_products():
    try:
        products = Product.query.all()
        dict_products = []
        for product in products:
            dict_products.append(product.to_dict())

        return jsonify({
            "products": dict_products
        })
    except Exception as e:
        return jsonify({
            "error": e
        }), 500