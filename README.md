# Animal-Flask
Flask side of a simple and social album reviewing site:
* Non-user can view the genres, albums and reviews.
* Only logged-in users will be able to create an album or update, and delete their own album though.
* Only logged-in users will be able to review an album, or update or delete their own reviews.
* User can register, thus logging in, can log in separately, and can log out.

## User Routes
* register route
user.route('/register', methods=['POST'])
// User will see that they are now registered.

* login route
user.route('/login', methods=['POST'])
// User will see that they are now logged in.

* User show route
user.route('/<id>', methods=['GET'])
// User will see their own reviews.

* Update route
user.route('/<id>', methods=['PUT'])
// User will be able to update their own information.


## Genre Routes

* displays the genre's
@albums.route('/genres/, methods=['GET'])
// Display's all genres

## Album Routes

* show albums once you click on the genre
@albums.route('/', methods=["GET"])
// Shows all albums in a specific genre.

* create album route
@albums.route('/<user>', methods=["POST"])
// User is able to add album DB to be reviewed.

* update album route
@albums.route('/<album>', methods=["PUT"])
// User is able to update the album itself.

## Review Routes

* create review route
@reviews.route('/<id>', methods=["POST"])
// Allows user to create review for album. 

* update review
@reviews.route('/<id>', methods=["PUT"])
// Allows user to be able to update thier past review of an album. 

* Delete review
@reviews.route('/<id>', methods=["Delete"])
// Allows user to delete their own review.
