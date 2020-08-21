from application import db
from application.models import email

db.drop_all()

db.create_all()