from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models.user import User
from app.extensions import db

admin_bp = Blueprint("admin", __name__)

def admin_required():
    return current_user.role == "admin"


@admin_bp.route("/admin")
@login_required
def admin_dashboard():

    if not admin_required():
        flash("Admin access only!")
        return redirect(url_for("dashboard.dashboard"))

    users = User.query.all()
    return render_template("admin_dashboard.html", users=users)


@admin_bp.route("/admin/delete/<int:user_id>")
@login_required
def delete_user(user_id):

    if not admin_required():
        return redirect(url_for("dashboard.dashboard"))

    user = User.query.get_or_404(user_id)

    # prevent admin deleting himself (important)
    if user.id == current_user.id:
        flash("You cannot delete yourself")
        return redirect(url_for("admin.admin_dashboard"))

    db.session.delete(user)
    db.session.commit()

    flash("User deleted successfully")
    return redirect(url_for("admin.admin_dashboard"))