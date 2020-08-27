from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):

    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_email_name(self):
        with patch('random.randrange') as r:
            r.return_value = 0
            response = self.client.get(url_for('get_name'))
            self.assertIn(b'Keynes', response.data)