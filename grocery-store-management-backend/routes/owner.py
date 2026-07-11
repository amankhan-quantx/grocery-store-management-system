from flask import Blueprint, render_template, session, redirect, url_for

from services.product_service import ProductService
from services.category_service import CategoryService

owner = Blueprint("owner", __name__)


@owner.route("/owner/dashboard")
def owner_dashboard():

    if "user" not in session:
        return redirect(url_for("auth.owner_login"))

    products = ProductService.get_products()

    categories = CategoryService.get_categories()

    total_products = len(products)

    total_categories = len(categories)

    low_stock = len(
        [product for product in products if product["quantity"] < 10]
    )

    out_of_stock = len(
        [product for product in products if product["quantity"] == 0]
    )

    return render_template(
        "owner/owner_dashboard.html",
        total_products=total_products,
        total_categories=total_categories,
        low_stock=low_stock,
        out_of_stock=out_of_stock
    )