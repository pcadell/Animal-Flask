import models

from flask import Blueprint, jsonify, request 
from flask_login import current_user, login_required 

from playhouse.shortcuts import model_to_dict

reviews = Blueprint('reviews', 'reviews')

# Allows user to create review for album.
@reviews.route('/<album_id>', methods=["POST"])
@login_required
def routes_index(album_id):
	payload = request.get_json()
	review = models.Review.create(album=album_id, content=payload['content'], user=current_user.id)
	review_dict = model_to_dict(review)
	review_dict['user'].pop('password')
	return jsonify(data=review_dict, status={"code": 201, "message":"Successfully reviewed the album!"}), 201



# Update reviews
@reviews.route('/<id>', methods=['PUT'])
@login_required
def update_review(id):
	payload = request.get_json()
	review = models.Review.get_by_id(id)
	if (review.user.id == current_user.id):
		review.content = payload['content']
		review.save()
		review_dict = model_to_dict(review)
		review_dict['user'].pop('password')
		return jsonify(data=review_dict, status={'code': 200, 'message': 'Review Successfully updated.'}), 201
	else:
		return jsonify(data='Forbidden', status={'code': 403, 'message': 'Only the Creator can update their reviews'}), 403
# Delete reviews 
@reviews.route('/<id>', methods=['Delete'])
@login_required
def delete_review(id):
	review_to_delete = models.Review.get_by_id(id)
	if review_to_delete.user.id != current_user.id:
		return jsonify(data="Forbidden", status={'code': 403, 'message': 'User can only delete their own review, man!'}), 403
	else: 
		review_to_delete.delete_instance()
		return jsonify(data='Review successfully deleted!', status={'code': 200, 'message': 'review successfully deleted'}), 200
