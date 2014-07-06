pip install https://www.djangoproject.com/download/1.7c1/tarball/

pip install -r requirements.txt
bower install

cd coins_project
./manage.py collectstatic
./manage.py syncdb
