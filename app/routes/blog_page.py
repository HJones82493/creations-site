from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

blog_page = Blueprint("blog_page", __name__, template_folder="../templates")


@blog_page.route("/blog", methods=["GET"])
def show():
    try:
        return render_template("blog.html")
    except TemplateNotFound:
        abort(404)
