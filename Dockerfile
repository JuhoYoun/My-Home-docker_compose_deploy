FROM python:3.9.0

WORKDIR /home/

RUN git clone git@github.com:JuhoYoun/My-Home-docker_compose_deploy.git

WORKDIR /home/My-Home-docker_compose_deploy/

RUN pip install -r requirements.txt

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=pinterest.settings.deploy && python manage.py migrate --settings=pinterest.settings.deploy && gunicorn pinterest.wsgi --env DJANGO_SETTINGS_MODULE=pinterest.settings.deploy --bind 0.0.0.0:8000"]














