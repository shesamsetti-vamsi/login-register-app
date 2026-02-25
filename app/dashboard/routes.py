from flask import Blueprint, render_template, flash
from flask_login import login_required, current_user
from app.extensions import db
from app.auth.forms import PasswordForm

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html", user=current_user)


@dashboard_bp.route("/profile", methods=["GET","POST"])
@login_required
def profile():
    form = PasswordForm()

    if form.validate_on_submit():
        current_user.set_password(form.password.data)
        db.session.commit()
        flash("Password updated successfully")

    return render_template("profile.html",
                           user=current_user,
                           form=form)