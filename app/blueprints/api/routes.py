from flask.globals import request
from .import bp as api
from flask import jsonify
from app.blueprints.shop.models import Product
from app import db
from .auth import basic_auth

@api.route('/products', methods=['GET'])
def get_products():
    """
    [GET] /api/products
    """
    return jsonify([p.to_dict() for p in Product.query.all()])

    
@api.route('/product/<int:id>', methods=['GET'])
def get_product(id):
    """
    [GET] /api/product/<id>
    """
    return jsonify(Product.query.get(id).to_dict())

@api.route('/product', methods=['POST'])
@basic_auth.login_required
def create_product():
    """
    [POST] /api/product
    """
    p = Product()
    data = {
        'name': request.get_json()['name'],
        'description': request.get_json()['description'],
        'image': request.get_json()['image'],
        'price': request.get_json()['price'],
    }
    p.from_dict(data)
    p.save()
    return jsonify(p.to_dict()), 201

@api.route('/product/<int:id>', methods=['PUT'])
@basic_auth.login_required
def update_products(id):
    """
    [PUT] /api/product/<id>
    """
    p = Product.query.get(id)
    data = {
        'name': request.get_json()['name'],
        'description': request.get_json()['description'],
        'image': request.get_json()['image'],
        'price': request.get_json()['price'],
    }
    p.from_dict(data)
    db.session.commit()
    return jsonify(p.to_dict())

@api.route('/product/<int:id>', methods=['DELETE'])
@basic_auth.login_required
def delete_product(id):
    """
    [DELETE] /api/product/<id>
    """
    p = Product.query.get(id)
    db.session.delete(p)
    db.session.commit()
    return jsonify([p.to_dict() for p in Product.query.all()])