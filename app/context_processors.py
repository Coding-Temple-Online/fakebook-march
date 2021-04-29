from app.blueprints.shop.models import Cart, Product
from flask_login import current_user
from flask import current_app as app

@app.context_processor
def build_cart():
    cart_dict = {}
    cart = Cart.query.filter_by(user_id=current_user.id).all()
    if len(cart) > 0:
        for i in cart:
            p = Product.query.get(i.product_id)
            if str(i.product_id) not in cart_dict:
                cart_dict[str(p.id)] = {
                    'id': i.id,
                    'product_id': p.id,
                    'quantity': 1,
                    'name': p.name,
                    'description': p.description,
                    'price': f"{p.price:.2f}",
                    'tax': p.tax
                }
            else:
                cart_dict[str(p.id)]['quantity'] += 1
    return {'cart_dict': cart_dict, 'cart_size': len(cart_dict)}