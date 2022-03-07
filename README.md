# Min-helper - Openclassrooms project 13


This project has been built with :

    - Django rest framework for the backend
    - Vuejs for the frontend
    - Docker / Heroku for the deployment


This project offers a platform for people to search for animes to watch.
A quick search can be done from the navbar, you will be able to filter the animes by category and score.
You will also be able to add animes to your favourites and write a comment in the detail page to share your thoughts about it.


The project can be seen at this address : https://rr-min-helper.herokuapp.com/



## Installation


Clone [the repository](https://github.com/Romderful/p13_min-helper) on your computer.

Be sure that you have docker installed on your computer, you can download it via the following link : https://www.docker.com/get-started


```bash

touch .env # create a file where you'll put your database configuration and the django secret key

DJANGO_SECRET_KEY="DJANGO_SECRET_KEY"
DB_NAME="DB_NAME"
DB_USER="DB_USER"
DB_PASSWORD="DB_PASSWORD"
DB_HOST="db"
DB_PORT="5432"
```


## Usage


```bash

docker-compose build # build the app under docker environment
docker-compose up # start the app
open a new terminal
docker-compose exec web python backend/manage.py migrate # migrate the database
docker-compose exec web python backend/manage.py createsuperuser # create the superuser credentials
docker-compose exec web python backend/manage.py fill_animes # populate the database with animes
```


## License


[MIT](https://choosealicense.com/licenses/mit/)