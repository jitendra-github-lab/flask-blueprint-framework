from flask import Blueprint
'''
Author: {{cookiecutter.Author}}
Email: {{cookiecutter.Email}}
Version: {{cookiecutter.Version}}
File Description = Please describe file related information here.
'''
example_one = Blueprint('example_1', __name__)


@example_one.route('/', methods=['GET'], strict_slashes=False)
def index():
    """method docstrings go here."""
    return 'Getting response from example one.'
