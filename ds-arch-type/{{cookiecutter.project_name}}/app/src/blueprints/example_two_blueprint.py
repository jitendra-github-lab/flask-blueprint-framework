from flask import Blueprint
from app.src.services.example_service_two import ServiceTwo
'''
Author: {{cookiecutter.Author}}
Email: {{cookiecutter.Email}}
Version: {{cookiecutter.Version}}
File Description = Please describe file related information here.
'''
example_two = Blueprint('example_2', __name__)


@example_two.route('/', methods=['GET'], strict_slashes=False)
def index():
    objs = ServiceTwo()
    output = objs.service_method()
    return output
