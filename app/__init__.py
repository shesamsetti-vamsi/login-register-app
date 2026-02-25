from flask import Flask
from app.config import Config
from app.extensions import db, bcrypt, login_manager, jwt
from app.models.user import User

def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    jwt.init_app(app)

    login_manager.login_view = "auth.login"

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register blueprints
    from app.auth.routes import auth_bp
    from app.dashboard.routes import dashboard_bp
    from app.admin.routes import admin_bp
    from app.api.auth_api import api_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(api_bp, url_prefix="/api")

    # CREATE DB + ADMIN USER
    with app.app_context():

        db.create_all()

        # AUTO ADMIN CREATION (SAFE)
        admin = User.query.filter_by(
            email="admin@email.com"
        ).first()

        if not admin:
            admin = User(
                username="admin",
                email="admin@email.com",
                role="admin"
            )
            admin.set_password("admin123")
            db.session.add(admin)
            db.session.commit()

            print("Admin created!")

    return app