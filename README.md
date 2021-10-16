# Django_MySQL_Docker

# Setup via Docker

1. First clone from repository:\
   `$ git clone https://github.com/KirillShapovalov/dj_my_do_project.git` \
   `$ cd dj_my_do_project`
2. Create a virtual environment: \
   `$ virtualenv env` \
   `$ source env/bin/activate`
3. Go to project folder: \
   `$ cd DjangoMySQLDocker`
4. Create your .env file with Django secret key, DB credentials and add API URLs for author/post synchronization: \
   _**url_posts=https://jsonplaceholder.typicode.com/posts**_ \
   **_url_authors=https://jsonplaceholder.typicode.com/users_**
5. Run docker container: \
   `$ docker-compose build` \
   `$ docker-compose up`
6. Server is running now, you're awesome.

# First step

In your browser navigate to http://localhost:8000/myApp/author/sync to synchronize authors
or http://localhost:8000/myApp/post/sync to synchronize posts.

# Authorization

1. To create new user go to **_../myApp/auth/users_** and fill the form with email, username and password for new user.
2. To authorize use Postman. Send **POST** request to **_../myApp/auth/token_** with username and password of existing
   user in parameters to get the auth-token and then add it to **Authorization** header for requests where authorization
   is required.

# CRUD

1. To get the list of all authors / posts go to  **_../myApp/authors_** or _**../myApp/posts**_ respectively.
2. To create new author go to **_../myApp/author/create/_** (_authorization required_).
3. To get the detail view of the author go to **_../myApp/author/id_**, where **_id_** is id of the author (_
   authorization required_).
4. To update the information about the author go to **_../myApp/author/update/id_**, where **_id_** is id of the
   author (_authorization required_).
5. To delete the author go to **_../myApp/author/delete/id_**, where **_id_** is id of the author (_authorization
   required_).
