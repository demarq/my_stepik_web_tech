cp -R etc/sites-available/* /etc/nginx/sites-available/

gunicorn -b 0.0.0.0:8000 --error-logfile /var/log/gunicorn/error.log --access-logfile /var/log/gunicorn/access.log ask.wsgi -D
gunicorn -b 0.0.0.0:8080 --error-logfile /var/log/gunicorn/error.log --access-logfile /var/log/gunicorn/access.log hello:app
service nginx restart

pip3 install django==2.0.6

service mysql start

mysql -uroot -e "create database django; create user django identified 
by 'qwerted'; grant all on django.* to django;"
