from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user
from app.extensions import db
from app.models.user import User
from app.auth.forms import RegisterForm, LoginForm

auth_bp = Blueprint("auth", __name__)

# REGISTER
@auth_bp.route("/register", methods=["GET", "POST"])
def register():

    # AUTO REDIRECT (important)
    if current_user.is_authenticated:
        return redirect(url_for("dashboard.dashboard"))

    form = RegisterForm()

    if form.validate_on_submit():

        user = User(
            username=form.username.data,
            email=form.email.data
        )
        user.set_password(form.password.data)

        db.session.add(user)
        db.session.commit()

        flash("Account created successfully")
        return redirect(url_for("auth.login"))

    return render_template("register.html", form=form)


# LOGIN
@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    # AUTO REDIRECT
    if current_user.is_authenticated:
        return redirect(url_for("dashboard.dashboard"))

    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        if user and user.check_password(form.password.data):
            login_user(user)

            # ADMIN AUTO REDIRECT
            if user.role == "admin":
                return redirect(url_for("admin.admin_dashboard"))

            return redirect(url_for("dashboard.dashboard"))

        flash("Invalid credentials")

    return render_template("login.html", form=form)


# LOGOUT
@auth_bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))