create virtual env 
``
pip install django
pip install mysqlclient
``

with docker 
``
docker-compose up --build
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate``


without docker
``
python manage.py runserver
``


I had to use cloud database to create tables, sinse csv files too large to upload
For the data analysis part : visit my kaggle notebook
https://www.kaggle.com/code/pataleenarasinghe/octopusbi

Had some difficulties understanding the data, some of them didnt make any sense.
I had to hardcode the sensitive data, and the dockerfiles. since this is getting evaluated.