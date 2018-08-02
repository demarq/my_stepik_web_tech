cp -R etc/sites-available/* /etc/nginx/sites-available/

gunicorn -b 0.0.0.0:8000 --error-logfile /var/log/gunicorn/error.log --access-logfile /var/log/gunicorn/access.log ask.wsgi -D
gunicorn -b 0.0.0.0:8080 --error-logfile /var/log/gunicorn/error.log --access-logfile /var/log/gunicorn/access.log hello:app
service nginx restart
