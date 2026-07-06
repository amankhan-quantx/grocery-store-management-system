from flask import Blueprint, render_template, request, redirect, url_for

from services.product_service import ProductService

products = Blueprint("products", __name__)


@products.route("/products")
def product_list():

    product_list = ProductService.get_products()

    return render_template(
        "products.html",
        products=product_list
    )


@products.route("/products/add", methods=["GET", "POST"])
def add_product():

    if request.method == "POST":

        ProductService.create_product(
            request.form["name"],
            request.form["category"],
            request.form["description"],
            float(request.form["price"]),
            int(request.form["quantity"]),
            request.form["image"],
            request.form["supplier"]
        )

        return redirect(url_for("products.product_list"))

    return render_template("add_product.html")