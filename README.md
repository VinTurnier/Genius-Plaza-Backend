Recipe App For Genius Place
===

Thank you for your cosidaration and the oportunity to take this challenge. I do hope you are pleased with me work and look forward to hearing your feedback. 

# Folder Structure
- The `core` directory contains the models
- The `user` directory contains user serializers, views, and urls for the user api
- The `recipe` directory contains the serializers, views, and urls for the recipe api

# Running the application
To make sure that we both are running the backend in the same environment, I created a `Dockerfile` to simplify our life. To run the application simply run:
```s
$ docker-compose up --build
```
This will build the image on your local machine, Then it will start running the `django-server`.

# Test
I've also included a couple model test, simply run:
```s
$ docker-compose run app sh -c "python manage.py test"
```
Just a couple test cases to test the model relationships

# Confusions
There was one thing that I was a little confused about. For the recipe orm model, the task asked to create a one to one relationship with user, which means that for one user there exists only one recipe. Yet on the API section there is one task that says get recipes by particular user. In this case I followed the API, and made a One to Many relationship between user and recipe. As that would be the simplest way to complete that task.