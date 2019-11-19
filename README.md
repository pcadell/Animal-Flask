# Animal-Flask
Flask side of an app to inform neighbors of Street Sweep schedule in their neighborhood
* Non-user can view the genres, albums and reviews.
* Only users will be able to Create, Update, and Delete their own review though.
* For this, they would need to register.
* User can register, thus logging in.
* User can add album information to the site.
* Any logged-in user can post a review of an album
* User can remove their own review of an album
* User can delete their own account
* If album or review outlive creator (user) account, it's attributed to "Anon"


# User Routes

* register route
user.route('/register', methods=['POST'])
// User will see that they are now registered.

* login route
user.route('/login', methods=['POST'])
// User will see that they are now logged in.

* User show route
user.route('/<id>', methods=['GET'])
// User will see their own reviews.

* update route
user.route('/<id>', methods=['PUT'])
// User will be able to update their own information.

* delete route
user.route('/<id>', methods=['Delete'])
// User will be able to delete their whole account.

# Genre Routes

* displays the genre's
@genres.route('/, methods=['GET'])
// Display's all genres

# Album Routes

* show albums once you click on the genre
@albums.route('/', methods=["GET"])
// Shows all albums in a specific genre.

* create album route
@albums.route('/<user_id>', methods=["POST"])
// User is able to add album DB to be reviewed.

* update album route
@albums.route('/<album_id>', methods=["PUT"])
// User is able to update the album itself.

# Review Routes

* create review route
@reviews.route('/<id>', methods=["POST"])
// Allows user to create review for album. 

* update review
@reviews.route('/<id>', methods=["PUT"])
// Allows user to be able to update thier past review of an album. 

* Delete review
@reviews.route('/<id>', methods=["Delete"])
// Allows user to delete their own review.
