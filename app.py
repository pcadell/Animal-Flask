from flask import Flask, jsonify, g

from flask_cors import CORS

from flask_login import LoginManager

DEBUG = True
PORT = 8000

app = Flask(__name__)

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