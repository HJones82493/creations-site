import os

from flask import Flask

from routes import main_page, gallery_page, order_page, blog_page

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_page.home_page)
    app.register_blueprint(gallery_page.gallery_page)
    app.register_blueprint(order_page.order_page)
    app.register_blueprint(blog_page.blog_page)

    socials = {
        'Facebook' : 'https://www.facebook.com',
        'Instagram' : 'https://www.instagram.com',
        'Pinterest' : 'https://www.pinterest.com'
    }

    @app.context_processor
    def inject_socials():
        return dict(
            Facebook=socials.get('Facebook'),
            Instagram=socials.get('Instagram'),
            Pinterest=socials.get('Pinterest')
        )
        
    return app


if __name__ == "__main__":
    host_name = os.environ.get("FLASK_HOST", "127.0.0.1")
    port = os.environ.get("FLASK_PORT", "5000")
    environment = os.environ.get("FLASK_ENV", "dev")

    print(host_name, port, environment)

    debug = False
    if environment == "dev":
        debug = True

    run_app = create_app()
    run_app.run(host=host_name, port=port, debug=debug)
