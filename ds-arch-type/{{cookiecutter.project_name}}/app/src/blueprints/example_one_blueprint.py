from flask import Blueprint, jsonify
from app.config.appconfig_parser import log_parser

'''
Author: {{cookiecutter.Author}}
Email: {{cookiecutter.Email}}
Version: {{cookiecutter.Version}}
File Description = Please describe file related information here.
'''

example_one = Blueprint('example_1', __name__)
logger = log_parser().getChild("example_one_blueprint")


@example_one.route('/', methods=['GET'], strict_slashes=False)
def index():
    """
    ---
    get:
      description: example_one_blueprint endpoint
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: OutputSchema
      tags:
          - Test GET Response from example_one_blueprint
    """
    output = 'Getting response from demo-one.';
    return jsonify(output)


@example_one.route('/index-two', methods=['GET'], strict_slashes=False)
def index_two():
    """
    ---
    get:
      description: example_one_blueprint endpoint
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: OutputSchema
      tags:
          - swagger response from example_one_blueprint
    """
    logger.debug("GET Method called 2")
    output = 'Getting response from demo-one index_two.';
    return jsonify(output)
    