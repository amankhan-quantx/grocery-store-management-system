from flask import Blueprint, render_template, session, redirect, url_for

owner = Blueprint("owner", __name__)


@owner.route("/owner/dashboard")
def owner_dashboard():

    if "user" not in session:
        return redirect(url_for("auth.login"))

    return render_template("owner/owner_dashboard.html")