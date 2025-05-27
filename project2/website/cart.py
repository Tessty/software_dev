
from flask import Blueprint, render_template, redirect, request, url_for, session
from flask_login import login_required, current_user
from website.models import CartItem, MenuItem, db

cart_bp = Blueprint('cart', __name__)

@cart_bp.route('/add_to_cart/<int:item_id>', methods=['POST'])
def add_to_cart(item_id):
    quantity = int(request.form.get('quantity', 1))
    if current_user.is_authenticated:
        existing_item = CartItem.query.filter_by(user_id=current_user.id, item_id=item_id).first()
        if existing_item:
            existing_item.quantity += quantity
        else:
            new_item = CartItem(user_id=current_user.id, item_id=item_id, quantity=quantity)
            db.session.add(new_item)
        db.session.commit()
    else:
        cart = session.get('cart', {})
        cart[str(item_id)] = cart.get(str(item_id), 0) + quantity
        session['cart'] = cart
    return redirect(url_for('views.menu'))

@cart_bp.route('/cart')
def view_cart():
    if current_user.is_authenticated:
        cart_items = CartItem.query.filter_by(user_id=current_user.id).all()
        total = sum(item.item.price * item.quantity for item in cart_items)
        return render_template('cart.html', cart_items=cart_items, total=total, is_guest=False)
    else:
        session_cart = session.get('cart', {})
        item_ids = [int(item_id) for item_id in session_cart.keys()]
        menu_items = MenuItem.query.filter(MenuItem.id.in_(item_ids)).all()

        cart_items = []
        total = 0
        for item in menu_items:
            qty = session_cart.get(str(item.id), 0)
            subtotal = item.price * qty
            total += subtotal
            cart_items.append({'item': item, 'quantity': qty, 'subtotal': subtotal})

        return render_template('cart.html', cart_items=cart_items, total=total, is_guest=True)

@cart_bp.route('/remove_cart_item/<int:item_id>')
def remove_cart_item(item_id):
    if current_user.is_authenticated:
        item = CartItem.query.filter_by(user_id=current_user.id, item_id=item_id).first()
        if item:
            db.session.delete(item)
            db.session.commit()
    else:
        cart = session.get('cart', {})
        if str(item_id) in cart:
            del cart[str(item_id)]
            session['cart'] = cart
    return redirect(url_for('cart.view_cart'))

@cart_bp.route('/update_quantity/<int:item_id>', methods=['POST'])
def update_quantity(item_id):
    new_qty = int(request.form.get('quantity', 1))
    if current_user.is_authenticated:
        cart_item = CartItem.query.filter_by(user_id=current_user.id, item_id=item_id).first()
        if cart_item:
            if new_qty < 1:
                db.session.delete(cart_item)
            else:
                cart_item.quantity = new_qty
            db.session.commit()
    else:
        cart = session.get('cart', {})
        if new_qty < 1:
            cart.pop(str(item_id), None)
        else:
            cart[str(item_id)] = new_qty
        session['cart'] = cart
    return redirect(url_for('cart.view_cart'))

@cart_bp.route('/checkout')
@login_required
def checkout():
    # In a real app, this is where you handle payments
    # For now, clear the cart and confirm the order
    cart_items = CartItem.query.filter_by(user_id=current_user.id).all()
    total = sum(item.item.price * item.quantity for item in cart_items)

    # Optional: Save order to Order table here

    # Clear the cart
    for item in cart_items:
        db.session.delete(item)
    db.session.commit()

    return render_template('checkout.html', total=total)

@cart_bp.route('/transfer_guest_cart')
@login_required
def transfer_guest_cart():
    session_cart = session.pop('cart', {})
    for item_id, quantity in session_cart.items():
        existing_item = CartItem.query.filter_by(user_id=current_user.id, item_id=int(item_id)).first()
        if existing_item:
            existing_item.quantity += quantity
        else:
            new_item = CartItem(user_id=current_user.id, item_id=int(item_id), quantity=quantity)
            db.session.add(new_item)
    db.session.commit()
    return redirect(url_for('cart.view_cart'))
