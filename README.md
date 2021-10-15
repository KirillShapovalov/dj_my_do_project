# Django_MySQL_Docker

# Setup

1. First clone from repository:\
   `$ git clone https://github.com/KirillShapovalov/dj_my_do_project.git` \
   `$ cd dj_my_do_project`
2. Create a virtual environment: \
   `$ virtualenv env` \
   `$ sourcre env/bin/activate`
3. Install the dependencies: \
   `(env)$ pip install -r requirements.txt`
4. Once pip has finished downloading the dependencies: \
   `(env)$ cd DjangoMySQLDocker` \
   `(env)$ python manage.py runserver`

# First step

In your browser first navigate to http://localhost:8000/app1/author/sync to synchronize authors and
then http://localhost:8000/app1/post/sync to synchronize posts.

# Authorization

1. To create new user go to **_../app1/auth/users_** and fill the form with email, username and password for new user.
2. To authorize use Postman. Send **POST** request to **_../app1/auth/token_** with username and password of existing
   user in parameters to get the auth-token and then add it to **Authorization** header for requests where authorization
   is required.

# CRUD

1. To get the list of all authors / posts go to  **_../app1/authors_** or _**../app1/posts**_ respectively.
2. To create new author go to **_../app1/author/create/_** (_authorization required_).
3. To get the detail view of the author go to **_../app1/author/id_**, where **_id_** is id of the author (_authorization required_).
4. To update the information about the author go to **_../app1/author/update/id_**, where **_id_** is id of the
   author (_authorization required_).
5. To delete the author go to **_../app1/author/delete/id_**, where **_id_** is id of the author (_authorization
   required_).
