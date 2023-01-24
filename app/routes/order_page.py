from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

order_page = Blueprint("order_page", __name__, template_folder="../templates")


@order_page.route("/order", methods=["GET"])
def show():
    try:
        return render_template("order.html")
    except TemplateNotFound:
        abort(404)
