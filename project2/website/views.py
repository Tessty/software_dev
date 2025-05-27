'''Install the route for the website'''

from flask import Blueprint, render_template, request, redirect, flash, url_for
from .models import Reservation
from .models import MenuItem
from .extension import db
from flask_login import login_required

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/gallery')
def gallery():
    return render_template("gallery.html")

@views.route('/reserve', methods=['GET', 'POST'])
def reserve():
    if request.method == 'POST':
        reservation = Reservation(
            name=request.form['name'],
            email=request.form['email'],
            phone=request.form['phone'],
            date=request.form['date'],
            time=request.form['time'],
            guests=request.form['guests'],
            message=request.form.get('message')
        )
        db.session.add(reservation)
        db.session.commit()
        flash('Reservation submitted successfully!')
        return redirect(url_for('views.home'))
    return render_template("reserve.html")


@views.route('/menu')
def menu():
    menu_items = MenuItem.query.all()
    print(f"🧪 Found {len(menu_items)} items in the database.")
    for item in menu_items:
        print(item.name, item.image)
    return render_template('menu.html', menu_items=menu_items)

@views.route('/admin')

@login_required
def admin():
    reservations = Reservation.query.order_by(Reservation.date).all()
    return render_template("admin.html", reservations=reservations)