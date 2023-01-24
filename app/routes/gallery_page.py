from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

gallery_page = Blueprint("gallery_page", __name__, template_folder="../templates")


@gallery_page.route("/gallery", methods=["GET"])
def show():
    try:
        return render_template("gallery.html")
    except TemplateNotFound:
        abort(404)
