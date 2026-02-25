from app.extensions import db, bcrypt
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(120), unique=True)
    password_hash = db.Column(db.String(200))
    role = db.Column(db.String(20), default="user")

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode()

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)