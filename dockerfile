FROM python:3.10-alpine

RUN pip install --no-cache-dir "Django>4.0,<5"
COPY . /app/
ADD requirements.txt requirements.txt
RUN pip install -t ./app -r requirements.txt
ENV PYTHONUNBUFFERED 1
RUN python /app/manage.py makemigrations
RUN python /app/manage.py migrate
CMD python /app/manage.py runserver 0.0.0.0:8000