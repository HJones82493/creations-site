from flask import Flask

from routes import main_page

def create_app():
	app = Flask(__name__)
	app.register_blueprint(main_page.home_page)

	return app

if __name__ == '__main__':
	run_app = create_app()
	run_app.run(debug=True)