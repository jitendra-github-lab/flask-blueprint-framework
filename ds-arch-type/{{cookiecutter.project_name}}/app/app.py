from flask import Flask, jsonify
from app.api_spec import spec
from app.src.blueprints.swagger import swagger_ui_blueprint, SWAGGER_URL
from app.config.appconfig_parser import log_parser

'''
Author: {{cookiecutter.Author}}
Email: {{cookiecutter.Email}}
Version: {{cookiecutter.Version}}
File Description = Please describe file related information here.
'''
logger = log_parser().getChild("app")

def create_app():
   
    from app.src.blueprints.example_one_blueprint import example_one
    from app.src.blueprints.example_two_blueprint import example_two

    app = Flask("{{cookiecutter.project_name}}", static_folder="app/assets")

    # Register blueprints {{cookiecutter.project_name}}
    app.register_blueprint(example_one, url_prefix='/api/one')  # URL should be http://server-ip:port/api/one
    app.register_blueprint(example_two, url_prefix='/api/two')  # URL should be http://server-ip:port/api/two
    app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

    @app.route("/")
    def hello():
        return "Hello, you have successfully configured your application, now you can use your full URL's to enjoy your" \
               " functionality!! "

    swagger_api(app)

    @app.errorhandler(404)
    @app.errorhandler(405)
    def page_not_found(ex):
        logger.error(str(ex))
        return jsonify(error=str(ex)), ex.code

    return app


def swagger_api(app):
    with app.test_request_context():
        # register all swagger documented functions here
        for fn_name in app.view_functions:
            if fn_name == 'static':
                continue
            print(f"Loading swagger docs for function: {fn_name}")
            view_fn = app.view_functions[fn_name]
            spec.path(view=view_fn)

    @app.route("/api/swagger.json")
    def create_swagger_spec():
        return jsonify(spec.to_dict())

