import datetime
from peewee import * 
from flask_login import UserMixin

DATABASE = SqliteDatabase('animal.sqlite')


class User(UserMixin, Model): 
	username = CharField(unique = True)
	email = CharField(unique = True)
	password = CharField()

	class Meta: 
		database = DATABASE

class Album(Model): 
	title = CharField()
	artist = CharField()
	user = ForeignKeyField(User, backref='albums')
	album_cover = CharField()	
	genre = CharField()
	created_at = DateTimeField(default=datetime.datetime.now)

	class Meta:
		database = DATABASE

class Review(Model):
	album = ForeignKeyField(Album, backref='reviews')
	user = ForeignKeyField(User, backref='reviews')
	content = CharField()
	created_at = DateTimeField(default=datetime.datetime.now)

	class Meta: 
		database = DATABASE

def initialize():
	DATABASE.connect()
	DATABASE.create_tables([User, Album, Review], safe=True)
	print("Created tables if they weren't already there")
	DATABASE.close()