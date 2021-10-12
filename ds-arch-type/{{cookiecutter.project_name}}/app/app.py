from flask import Flask, jsonify

'''
Author: {{cookiecutter.Author}}
Email: {{cookiecutter.Email}}
Version: {{cookiecutter.Version}}
File Description = Please describe file related information here.
'''

def create_app():
    from app.src.blueprints.example_one_blueprint import example_one
    from app.src.blueprints.example_two_blueprint import example_two

    app = Flask("ds-arch-type", static_folder="app/assets")

    # Register blueprints {{cookiecutter.project_name}}
    app.register_blueprint(example_one, url_prefix='/api/one')  # URL should be http://server-ip:port/api/one
    app.register_blueprint(example_two, url_prefix='/api/two')  # URL should be http://server-ip:port/api/two

    @app.route("/")
    def hello():
        return "Hello, you have successfully configured your application, now you can use your full URL's to enjoy your" \
               " functionality!! "

    @app.errorhandler(404)
    @app.errorhandler(405)
    def page_not_found(ex):
        return jsonify(error=str(ex)), ex.cod

    return app

