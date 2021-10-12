import unittest
from app.src.services.example_service_two import ServiceTwo


class TestServiceTwo(unittest.TestCase):
    def test_something(self):
        obj = ServiceTwo()
        output = obj.service_method()
        print("OUTPUT ", output)
        assert isinstance(output, str)


# if __name__ == '__main__':
#     unittest.main()
