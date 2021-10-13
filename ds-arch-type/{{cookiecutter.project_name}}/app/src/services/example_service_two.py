'''
Author = {{cookiecutter.Author}}
Email = {{cookiecutter.Email}}
Version {{cookiecutter.Version}}
File Description = Please describe file related information here.
'''

class ServiceTwo:

    def service_method(self, data):
        """

        :param data:
        :return: json
        """
        name = data['name']
        output = {"msg": f"Testing is done successfully : '{name}'"}
        return output
