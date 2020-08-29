from application import db
from datetime import datetime

#  creates the database
class email(db.Model):
	id = db.Column(db.Integer, primary_key=True,autoincrement=True)
	gen_email = db.Column(db.String(30), nullable=False)
	
	def __repr__(self):
		return ' '.join(['Email:',self.gen_email])