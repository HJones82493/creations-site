import os

from flask import Flask

from routes import main_page


def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_page.home_page)

    return app


if __name__ == "__main__":
    host_name = os.environ.get("FLASK_HOST", "127.0.0.1")
    port = os.environ.get("FLASK_PORT", "5000")
    environment = os.environ.get("FLASK_ENV", "dev")

    debug = False
    if environment == "dev":
        debug = True

    run_app = create_app()
    run_app.run(host=host_name, port=port, debug=debug)
