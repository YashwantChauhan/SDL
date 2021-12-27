FROM python:3.8-slim-buster
WORKDIR /
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD python manage.py runserver 0.0.0.0:$PORT