import models

from flask import Blueprint, jsonify, request 
from flask_login import current_user, login_required 

from playhouse.shortcuts import model_to_dict

albums = Blueprint('albums', 'albums')


# list genres
@albums.route('/genres/', methods=["GET"])
def genres_index():
	try:
		genres = models.Album.select(models.Album.genre).group_by(models.Album.genre)
		genres_to_dict = [model_to_dict(genre) for genre in genres]
		return jsonify(data=genres_to_dict, status={"code": 200, "message": "Successfully found genres"}), 200
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
	album = models.Album.create(title=payload['title'], artist=payload['artist'], album_cover=payload['album_cover'], genre=payload['genre'], user=current_user.id)

	album_dict = model_to_dict(album)
	album_dict['user'].pop('password')

	return jsonify(data=album_dict, status={'code': 201, 'message':'Successfully created album, {}'.format(album_dict['title'])}), 201

# show album route
@albums.route('/<id>', methods=['GET'])
def get_one_album(id):
	album = models.Album.get_by_id(id)
	reviews=[]

	reviews = album.reviews

	reviews = [model_to_dict(r) for r in reviews]

	if not current_user.is_authenticated:
		return jsonify(data={'title': album.title, 'artist': album.artist, 'genre': album.genre, 'album_cover': album.album_cover}, status={'code': 200, 'message': "Registered users can access reviews of these albums, wink wink."}), 200
	else:
		album_dict = model_to_dict(album)
		album_dict['user'].pop('password')
		return jsonify(data={'album': album_dict, 'reviews': reviews}, status={'code': 200, 'message': 'Found album by id {}'.format(album.id)}), 200 

# update album route 
@albums.route('/<id>', methods=["PUT"])
@login_required
def update_album(id):
	payload = request.get_json()
	album = models.Album.get_by_id(id)
	if(album.user.id == current_user.id):
		album.title = payload['title'] if 'title' in payload else None
		album.artist = payload['artist'] if 'artist' in payload else None 
		album.album_cover = payload['album_cover'] if 'album_cover' in payload else None 
		album.genre = payload['genre'] if 'genre' in payload else None 
		album.save()
		album_dict = model_to_dict(album)
		album_dict['user'].pop('password')
		return jsonify(data=album_dict, status={'code': 200, 'message': 'Album updated successfully!'}),200
	else:
		return jsonify(data="Forbidden", status={'code': 403, 'message': "Only the user that created this album can update it! Get outta here!"}), 403
