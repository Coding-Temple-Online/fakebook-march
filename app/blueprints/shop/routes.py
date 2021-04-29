from flask import render_template, redirect, url_for, current_app as app, flash, request
from . import bp as shop
import stripe
from .models import Product, Cart, Order
from app.seed import seed_data
from flask_login import current_user
from app.context_processors import build_cart

stripe.api_key = app.config.get('STRIPE_SECRET_KEY')

@shop.route('/seed')
def seed():
    seed_data()
    flash('Your product data has been seeded.', 'primary') 
    return redirect(url_for('shop.index'))

@shop.route('/')
def index():
    context = {
        'products': [p.to_dict() for p in Product.query.all()]
    }
    return render_template('shop/index.html', **context)

@shop.route('/cart/add')
def add_to_cart():
    try:
        p = Product.query.get(request.args.get('product_id'))
        item = Cart(user_id=current_user.get_id(), product_id=p.id)
        item.save()
        flash(f"{p.name} has been added successfully", 'success')
    except Exception as err:
        flash(f"There was an error adding the {p.name}", 'danger')
        print(err)
    return redirect(url_for('shop.index'))

@shop.route('/cart')
def cart():
    display_cart = build_cart()['cart_dict']
    print(display_cart)
    context = {
        'cart': display_cart.values()
    }
    return render_template('shop/cart.html', **context)