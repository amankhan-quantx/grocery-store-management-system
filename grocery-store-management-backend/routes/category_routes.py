from flask import Blueprint, render_template, request, redirect, session, url_for

from services.category_service import CategoryService

categories = Blueprint("categories", __name__)


@categories.route("/owner/categories")
def owner_categories():

    if "user" not in session:
        return redirect(url_for("auth.owner_login"))

    category_list = CategoryService.get_categories()

    return render_template(
        "owner/owner_categories.html",
        categories=category_list
    )


@categories.route("/owner/categories/add", methods=["GET", "POST"])
def owner_add_category():

    if "user" not in session:
        return redirect(url_for("auth.owner_login"))

    if request.method == "POST":

        try:

            CategoryService.create_category(
                request.form["name"]
            )

            return redirect(
                url_for("categories.owner_categories")
            )

        except ValueError as error:

            return render_template(
                "owner/owner_add_category.html",
                error=str(error)
            )

    return render_template("owner/owner_add_category.html")

@categories.route("/owner/categories/delete/<int:category_id>")
def owner_delete_category(category_id):

    if "user" not in session:
        return redirect(url_for("auth.owner_login"))

    try:

        CategoryService.delete_category(category_id)

    except ValueError:
        pass

    return redirect(url_for("categories.owner_categories"))

@categories.route("/owner/categories/edit/<int:category_id>", methods=["GET", "POST"])
def owner_edit_category(category_id):

    if "user" not in session:
        return redirect(url_for("auth.owner_login"))

    category = CategoryService.get_category(category_id)

    if not category:
        return redirect(url_for("categories.owner_categories"))

    if request.method == "POST":

        try:

            CategoryService.update_category(
                category_id,
                request.form["name"]
            )

            return redirect(
                url_for("categories.owner_categories")
            )

        except ValueError as error:

            return render_template(
                "owner/owner_edit_category.html",
                category=category,
                error=str(error)
            )

    return render_template(
        "owner/owner_edit_category.html",
        category=category
    )