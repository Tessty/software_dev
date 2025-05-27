# Set up flask
from flask import Flask
from flask_login import LoginManager
from .extension import db
from .models import User
from .cart import cart_bp


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secretkey'

     # PostgreSQL database connection
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost/project2DB'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize db with app
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
 
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .views import views
    from .auth import auth


    app.register_blueprint(auth)
    app.register_blueprint(cart_bp)
    app.register_blueprint(views, url_prefix='/')
    


    
    with app.app_context():
        db.create_all()
    
    return app