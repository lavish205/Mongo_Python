from flask import Flask
from flask.ext.mongoengine import MongoEngine


db = MongoEngine()

def create_app():
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_object('configurations.Development')
	
	db.init_app(app)

	return app