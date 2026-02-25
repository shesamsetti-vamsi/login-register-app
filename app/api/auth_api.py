from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from app.models.user import User

api_bp = Blueprint("api", __name__)

@api_bp.route("/login", methods=["POST"])
def api_login():
    data = request.get_json()

    user = User.query.filter_by(email=data["email"]).first()

    if user and user.check_password(data["password"]):
        token = create_access_token(identity=user.id)
        return jsonify(access_token=token)

    return jsonify({"msg": "Invalid credentials"}), 401