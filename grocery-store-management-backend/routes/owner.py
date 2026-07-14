from flask import Blueprint, render_template, session, redirect, url_for

from services.product_service import ProductService
from services.category_service import CategoryService

owner = Blueprint("owner", __name__)


@owner.route("/owner/dashboard")
def owner_dashboard():

    if "user" not in session:
        return redirect(url_for("auth.owner_login"))

    total_products = ProductService.get_total_products()

    total_categories = len(
        CategoryService.get_categories()
    )

    low_stock_products = ProductService.get_low_stock()

    out_of_stock_products = ProductService.get_out_of_stock()

    recent_products = ProductService.get_recent_products()

    expired_products = ProductService.get_expired_products()

    expiring_soon_products = ProductService.get_expiring_soon_products()

    return render_template(
        "owner/owner_dashboard.html",
        total_products=total_products,
        total_categories=total_categories,
        low_stock=len(low_stock_products),
        out_of_stock=len(out_of_stock_products),
        low_stock_products=low_stock_products,
        out_of_stock_products=out_of_stock_products,
        recent_products=recent_products,
        expired_products=expired_products,
        expiring_soon_products=expiring_soon_products
    )