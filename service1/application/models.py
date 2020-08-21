from application import db
from datetime import datetime
# export DATABASE_URI="mysql+pymysql://root:root@35.246.10.208:3306/animal_db"
# export SECRET_KEY=fasdfadsfadsfwaefsadv43tw4

class email(db.Model):
	id = db.Column(db.Integer, primary_key=True,autoincrement=True)
	gen_email = db.Column(db.String(30), nullable=False)