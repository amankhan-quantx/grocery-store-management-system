import os
from datetime import datetime, timedelta

from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    session,
    url_for,
    current_app
)

from werkzeug.utils import secure_filename

from services.product_service import ProductService
from services.category_service import CategoryService

products = Blueprint("products", __name__)


@products.route("/owner/products")
def product_list():

    if "user" not in session:
        return redirect(url_for("auth.owner_login"))

    keyword = request.args.get("search", "").strip()

    if keyword:
        product_list = ProductService.search_products(keyword)
    else:
        product_list = ProductService.get_products()

    today = datetime.today().date()

    products_data = []

    for product in product_list:

        product = dict(product)

        expiry = product.get("expiry_date")

        product["expiry_status"] = "No Expiry"

        if expiry:

            expiry_date = datetime.strptime(
                expiry,
                "%Y-%m-%d"
            ).date()

            if expiry_date < today:

                product["expiry_status"] = "Expired"

            elif expiry_date <= today + timedelta(days=7):

                product["expiry_status"] = "Expiring Soon"

            else:

                product["expiry_status"] = "Fresh"

        products_data.append(product)

    return render_template(
        "owner/owner_products.html",
        products=products_data,
        search=keyword
    )


@products.route("/owner/products/add", methods=["GET", "POST"])
def add_product():

    if "user" not in session:
        return redirect(url_for("auth.owner_login"))

    categories = CategoryService.get_categories()

    if request.method == "POST":

        image = request.files["image"]

        filename = ""

        if image and image.filename:

            filename = secure_filename(image.filename)

            upload_folder = os.path.join(
                current_app.static_folder,
                "uploads"
            )

            image.save(
                os.path.join(upload_folder, filename)
            )

        ProductService.create_product(
            request.form["name"],
            int(request.form["category_id"]),
            request.form["description"],
            float(request.form["price"]),
            int(request.form["quantity"]),
            request.form["supplier"],
            request.form["barcode"],
            request.form["expiry_date"],
            filename
        )

        return redirect(
            url_for("products.product_list")
        )

    return render_template(
        "owner/owner_add_product.html",
        categories=categories
    )


@products.route("/owner/products/edit/<int:product_id>", methods=["GET", "POST"])
def edit_product(product_id):

    if "user" not in session:
        return redirect(url_for("auth.owner_login"))

    product = ProductService.get_product(product_id)

    categories = CategoryService.get_categories()

    if request.method == "POST":

        image = request.files["image"]

        filename = product["image"]

        if image and image.filename:

            filename = secure_filename(image.filename)

            upload_folder = os.path.join(
                current_app.static_folder,
                "uploads"
            )

            image.save(
                os.path.join(upload_folder, filename)
            )

        ProductService.update_product(
            product_id,
            request.form["name"],
            int(request.form["category_id"]),
            request.form["description"],
            float(request.form["price"]),
            int(request.form["quantity"]),
            request.form["supplier"],
            request.form["barcode"],
            request.form["expiry_date"],
            filename
        )

        return redirect(
            url_for("products.product_list")
        )

    return render_template(
        "owner/owner_edit_product.html",
        product=product,
        categories=categories
    )


@products.route("/owner/products/delete/<int:product_id>")
def delete_product(product_id):

    if "user" not in session:
        return redirect(url_for("auth.owner_login"))

    ProductService.delete_product(product_id)

    return redirect(
        url_for("products.product_list")
    )