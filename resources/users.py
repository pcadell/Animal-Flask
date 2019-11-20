import models 

from flask import request, jsonify, Blueprint
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user, LoginManager
from playhouse.shortcuts import model_to_dict



users = Blueprint('users', 'users')

@users.route('/register', methods=["POST"])
def register():
	payload = request.get_json()
	payload['email'].lower()

	try:
		models.User.get(models.User.email == payload['email'])
		return jsonify(data={}, status={"code": 401, "message": "A user with that email has already register with our wonderful app"}), 401
	except models.DoesNotExist:
		payload['password'] = generate_password_hash(payload['password'])
		user = models.User.create(**payload)

		login_user(user)

		user_dict = model_to_dict(user)
		print(user_dict)
		del user_dict['password']
		return jsonify(data=user_dict, status={'code': 201, "message": "You monster! You've created a user with the email of {}".format(user_dict['email'])}), 201

@users.route('/login', methods=["PUT"])
def login():
	payload = request.get_json()
	try:
		user = models.User.get(models.User.email == payload['email'])
		user_dict = model_to_dict(user)
		if(check_password_hash(user_dict['password'], payload['password'])):
			login_user(user)
			del user_dict['password']
			return jsonify(data=user_dict, status={'code': 200, 'message': "Successfully logged in {}".format(user_dict['email'])}), 200
		else: 
			print('password invalid')
			return jsonify(data={}, status={'code': 401, 'message': "Email or password is incorrect"}), 401
	except models.DoesNotExist:
		print('email not found')
		return jsonify(data={}, status={'code':401, 'message': 'Email or password is incorrect'}), 401

@users.route('/', methods=["GET"])
def list_users():
	users = models.User.select()
	for u in users:
		print(u)

	user_dicts = [model_to_dict(u) for u in users]
	def remove_password(u):
		u.pop('password')
		return u 

	user_dicts_without_pw = list(map(remove_password, user_dicts))
	return jsonify(data=user_dicts_without_pw), 200

@users.route('/logged_in', methods=["GET"])
def get_logged_in_user():
	if not current_user.is_authenticated:
		return jsonify(data={}, status={'code': 401, 'message': "No one is currently shredding"}), 401
	else: 
		user_dict = model_to_dict(current_user)
		user_dict.pop('password')
		return jsonify(data=user_dict, status={'code': 200, 'message': "Current shredder is {}".format(user_dict['email'])}), 200

@users.route('/logout', methods=['GET'])
def logout():
	email = model_to_dict(current_user)['email']
	logout_user()
	return jsonify(data={}, status={'code': 200, 'message': "Successfully logged out {}".format(email)})