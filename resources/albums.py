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
@login_required
def create_albums():
	payload = request.get_json()
	album = models.Album.create(title=payload['title'], artist=payload['artist'], album_cover=payload['album_cover'], genre=payload['genre'], user_id=current_user.id)

	album_dict = model_to_dict(album)
	album_dict['user_id'].pop('password')

	return jsonify(data=album_dict, status={'code': 201, 'message':'Successfully created album, {}'.format(album_dict['title'])}), 201

# show album route
@albums.route('/<id>', methods=['GET'])
def get_one_album(id):
	album = models.Album.get_by_id(id)

	if not current_user.is_authenticated:
		return jsonify(data={'title': album.title, 'artist': album.artist, 'genre': album.genre, 'album_cover': album.album_cover}, status={'code': 200, 'message': "Registered users can access reviews of these albums, wink wink."}), 200
	else:
		album_dict = model_to_dict(album)
		album_dict['user_id'].pop('password')
		return jsonify(data=album_dict, status={'code': 200, 'message': 'Found album by id {}'.format(album.id)}), 200