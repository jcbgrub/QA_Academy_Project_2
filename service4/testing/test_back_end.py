from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):

	def create_app(self):
		return app

class TestResponse(TestBase):

	def test_sputnik(self):
		with patch('requests.get') as g:
			g.return_value.text = "test12"
			response = self.client.post(url_for('get_email'),data='test12')
			self.assertIn(b'test12@sputnik.com', response.data)

	def test_cosmonaut(self):
		with patch('requests.get') as g:
			g.return_value.text = "test1234"
			response = self.client.post(url_for('get_email'),data='test1234')
			self.assertIn(b'test1234@cosmonaut.com', response.data)

	def test_spacerocket(self):
		with patch('requests.get') as g:
			g.return_value.text = "test1234567"
			response = self.client.post(url_for('get_email'),data='test1234567')
			self.assertIn(b'test1234567@spacerocket.com', response.data)

	# def test_else(self):
	# 	with patch('requests.get') as g:
	# 		g.return_value.text = "3"
	# 		# response = self.client.post(url_for('get_email'),data='3')
	# 		self.assertIn(b'this should not be here', response.data)