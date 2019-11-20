from flask import Flask, jsonify, g

import models 

from flask_cors import CORS

from flask_login import LoginManager

from resources.albums import albums 
from resources.reviews import reviews 
from resources.users import users

CORS(albums, origins=['http://localhost:3000'], supports_credentials=True)
CORS(reviews, origins=['http://localhost:3000'], supports_credentials=True)
CORS(users, origins=['http://localhost:3000'], supports_credentials=True)

app.register_blueprint(albums, url_prefix='/api/v1/albums')
app.register_blueprint(reviews, url_prefix='/api/v1/reviews')
app.register_blueprint(users, url_prefix='/api/v1/users')

DEBUG = True
PORT = 8000

app = Flask(__name__)

app.secret_key = "This is a long sentence that holds no value"

@app.before_request
def before_request():
	g.db = models.DATABASE
	g.db.connect()

@app.after_request
def after_request(response):
	g.db.close()
	return response

@app.route('/test')
def test_route():
	return ['Heres the test route']

if __name__ == '__main__':
	models.initialize()
	app.run(debug=DEBUG, port=PORT)