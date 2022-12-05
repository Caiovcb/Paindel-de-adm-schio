FROM python:3.10
ENV PYTHONUNBUFFERED=1

RUN apt-get install default-libmysqlclient-dev
RUN pip install --upgrade pip

COPY dadoste/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY . /app/


WORKDIR /app 

CMD python /app/manage.py runserver 0.0.0.0:8000