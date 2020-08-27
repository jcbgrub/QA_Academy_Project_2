import unittest
from flask import url_for
from os import getenv
from unittest.mock import patch
from flask_testing import TestCase
from application import app, db
from application.models import email

class TestBase(TestCase):
	def create_app(self):
		app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DATABASE_URI'),
		SECRET_KEY=getenv('TEST_SECRET_KEY'),
		WTF_CSRF_ENABLED=False,
		DEBUG=True
		)
		return app
	
	def setUp(self):
		# clear database
		db.session.commit()
		db.drop_all()
		db.create_all()

		# Creating a test team
		testemail = email(
			id = 1,
			gen_name = "test12@test.com"
		)
		# save team to database
		db.session.add(testemail)
		db.session.commit()

	def tearDown(self):
		# run down test 
		db.session.remove()
		db.drop_all()

class Test_Service1(TestBase):
	def test_generate_view(self):
		response = self.client.get(url_for("home"))
		self.assertEqual(response.status_code, 200)
		self.assertIn(b"All Emails", response.data)
	
	def test_generate_email(self):
		with patch('requests.get') as g:
			g.return_value.text = 'Rosa'
			with patch('requests.post') as p:
			  p.return_value.text = '5'
			  response = self.client.get(url_for("generate"))
			  self.assertEqual(response.status_code, 200)
			  self.assertIn(b"Rosa5", response.data)

	def test_view_emails(self):
		response = self.client.get(url_for("home"))
		self.assertEqual(response.status_code, 200)
		print(response.data)
		self.assertIn(b"All Emails", response.data)