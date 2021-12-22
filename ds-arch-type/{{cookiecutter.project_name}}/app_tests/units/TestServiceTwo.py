import unittest
import json
from app.src.services.example_service_two import ServiceTwo


class TestServiceTwo(unittest.TestCase):

    def test_post_method_request_and_response(self):
        obj = ServiceTwo()
        jsonmsg = '{"name":"Jeet"}'
        data = json.loads(jsonmsg)

        output = obj.service_method(data)

        assert isinstance(json.loads(output), dict)


# if __name__ == '__main__':
#     unittest.main()
