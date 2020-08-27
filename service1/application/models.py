from application import db
from datetime import datetime
# export DATABASE_URI="mysql+pymysql://root:root@35.246.94.253:3306/emaildb"
# export TEST_DATABASE_URI="mysql+pymysql://root:root@35.246.94.253:3306/emaildbtest"
# SECRET_KEY="fasdfadsfadsfwaefsadv43tw777774"
# TEST_SECRET_KEY="fasdfadsfadsfwaefsadv43tw4"



class email(db.Model):
	id = db.Column(db.Integer, primary_key=True,autoincrement=True)
	gen_email = db.Column(db.String(30), nullable=False)
	
	def __repr__(self):
		return ' '.join(['Email:',self.gen_email])