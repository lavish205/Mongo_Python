from todo import db

class User(db.Document):
	username = db.StringField(required=True)
	password = db.StringField(required=True)

class Task(db.EmbeddedDocument):
	title = db.StringField(required=True)
	is_active = db.BooleanField(required=True)


class Todo(db.Document):
	username = db.ReferenceField(User)
	todo_list = db.ListField(Task)
