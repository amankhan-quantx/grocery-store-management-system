import os
from flask import Flask, session, redirect, url_for

from config import Config
from routes.auth import auth
from routes.products import products
from routes.owner import owner
from routes.category_routes import categories

BASE_DIR = os.path.dirname(__file__)

FRONTEND_DIR = os.path.join(
    BASE_DIR,
    "..",
    "grocery-store-management-frontend"
)

app = Flask(
    __name__,
    template_folder=os.path.join(FRONTEND_DIR, "templates"),
    static_folder=os.path.join(FRONTEND_DIR, "static")
)

app.config.from_object(Config)

# Register Blueprints
app.register_blueprint(auth)
app.register_blueprint(products)
app.register_blueprint(owner)
app.register_blueprint(categories)


@app.route("/")
def home():

    if "user" not in session:
        return redirect(url_for("auth.owner_login"))

    return redirect(url_for("owner.owner_dashboard"))


if __name__ == "__main__":
    app.run(debug=True)