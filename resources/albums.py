import models 

from flask import Blueprint, jsonify, request 
from flask_login import current_user, login_required 

from playhouse.shortcuts import model_to_dict

albums = Blueprint('albums', 'albums')


# list genres
@albums.route('/', methods=["GET"])
def genres_index():
	try:
		genres = models.Album.genre.select()
		print(genres)
		return jsonify(data=genres, status={"code": 201, "message": "Successfully found genres"}), 201
	except models.DoesNotExist:
		return jsonify(data={}, status={"code": 401, "message": "Error getting albums. WTF?"}), 401
	

# list albums as an index
@albums.route('/', methods=["GET"])
def albums_index():
	try: 
		albums = [model_to_dict(albums) for albums in models.Album.select()]
		print(albums)
		return jsonify(data=albums, status={"code": 200, "message": "Success"}), 200
	except models.DoesNotExist:
		return jsonify(data={}, status={"code": 401, "message": "error getting the resources"}), 401

# create album route
@albums.route('/', methods=["POST"])
def create_albums():
	payload = request.get_json()
	album = models.Album.create(**payload)
	print(album.__dict__)
	print(dir(album))
	album_dict = model_to_dict(album)
	return jsonify(data=album_dict, status={"code": 201, "message": "Success"}), 201