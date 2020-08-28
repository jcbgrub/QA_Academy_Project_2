from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):

	def create_app(self):
		return app

class TestResponse(TestBase):

	def test_sputnik(self):
	# We will mock a response of 1 and test that we get football returned.
		with patch('requests.get') as g:
			g.return_value.text = "test12"
			response = self.client.get(url_for('get_email'))
			self.assertIn(b'test12@sputnik.com', response.data)


		#         def test_team_slogan(self): 
		# with patch('requests.get') as i:
		#         i.return_value.text = 'London'
		#         with patch('random.randrange') as r:
		#             r.return_value = 1
		#             response = self.client.post(
		#             url_for('get_slogan'),
		#             data = 'London')
		#             self.assertIn(b'Win from Within.', response.data)