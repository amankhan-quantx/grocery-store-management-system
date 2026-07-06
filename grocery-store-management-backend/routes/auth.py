from flask import Blueprint, render_template, request, redirect, session, url_for
from werkzeug.security import check_password_hash

from models.user import User

auth = Blueprint("auth", __name__)


# ==========================
# Owner Login
# ==========================
@auth.route("/owner/login", methods=["GET", "POST"])
def owner_login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        user = User.get_by_username(username)

        if (
            user
            and user["role"] == "owner"
            and check_password_hash(user["password_hash"], password)
        ):

            session["user"] = user["username"]
            session["role"] = user["role"]

            return redirect(url_for("owner.owner_dashboard"))

        return render_template(
            "owner/owner_login.html",
            error="Invalid username or password."
        )

    return render_template("owner/owner_login.html")


# ==========================
# Customer Login
# (Version 1 - Placeholder)
# ==========================
@auth.route("/customer/login", methods=["GET", "POST"])
def customer_login():

    return render_template("customer/customer_login.html")


# ==========================
# Logout
# ==========================
@auth.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("auth.owner_login"))