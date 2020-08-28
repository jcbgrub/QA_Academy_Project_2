  
from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_team_number(self):
        with patch('random.randint') as r:
            r.return_value = 1
            response = self.client.get(url_for('get_number'))
            self.assertIn(b'1', response.data)
