import unittest
import requests


class TestServiceOne(unittest.TestCase):

    def test_service_one_to_check_status_code_200(self):
        response = requests.get("http://localhost:5000/api/one")
        assert response.status_code == 200


