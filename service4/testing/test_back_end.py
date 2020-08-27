from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):

    def create_app(self):
        return app

    def test_team_slogan(self): 
            with patch('requests.get') as i:
                i.return_value.text = 'London'
                response = self.client.get(url_for('get_email'))
                self.assertIn(b'London', response.data)    
            with patch('random.randrange') as r:
                r.return_value = 1
                response = self.client.get(
                url_for('get_slogan'),
                data = city)
                self.assertIn(b'Win from Within.', response.data)
                self.assertIn(b'London', response.data) 