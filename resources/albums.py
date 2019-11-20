import models 

from flask import Blueprint, jsonify, request 
from flask_login import current_user, login_required 

from playhouse.shortcuts import model_to_dict

albums = Blueprint('albums', 'albums')

@albums.route('/' methods=["GET"])
def albums_index():
	try: 
		albums = [model_to_dict(albums) for albums in models.Album.select()]
		print(albums)
		return jsonify(data=albums, status={"code": 200, "message": "Success"})
	except models.DoesNotExist:
		return jsonify(data={}, status={"code": 401, "message": "error getting the resources"})