FROM python:3.10.10

ENV PYTHONUNBUFFERED 1

WORKDIR /feu-backend

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . . 

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:9000