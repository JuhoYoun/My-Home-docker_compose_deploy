FROM python:3.9.0

RUN mkdir /root/.ssh/

# 이미지를 가지는 사람은 private key 또한 입수 가능 !
ADD ./.ssh/id_rsa /root/.ssh/id_rsa

RUN chmod 600 /root/.ssh/id_rsa

RUN touch /root/.ssh/known_hosts

RUN ssh-keyscan github.com >> /root/.ssh/known_hosts

WORKDIR /home/

RUN git clone git@github.com:JuhoYoun/My-Home.git

WORKDIR /home/My-Home/

RUN pip install -r requirements.txt

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=pinterest.settings.deploy && python manage.py migrate --settings=pinterest.settings.deploy && gunicorn pinterest.wsgi --env DJANGO_SETTINGS_MODULE=pinterest.settings.deploy --bind 0.0.0.0:8000"]














