@shop.route('/react/checkout', methods=['POST'])
def checkout_react():
    data = ast.literal_eval(request.get_data().decode('UTF-8'))
    l_items = []
    for product in data['items'].values():
        # print(int(product['info']['price'] * 100))
        product_dict = {
            'price_data': {
                'currency': 'usd',
                'unit_amount': int(product['info']['price'] * 100),
                'product_data': {
                    'name': product['info']['name'],
                    'images': [product['info']['image']],
                },
            },
            'quantity': product['quantity'],
        }
        l_items.append(product_dict)
    
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=l_items,
            mode='payment',
            success_url='http://127.0.0.1:3000/shop/cart',
            cancel_url='http://127.0.0.1:3000/shop/cart',
        )
        return jsonify({'session_id': checkout_session.id})
    except Exception as e:
        return jsonify(error=str(e)), 403