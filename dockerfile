FROM python:3.10-alpine


COPY dadoste/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY dadoste/ /app/

ENV PYTHONUNBUFFERED 1
WORKDIR /app 

CMD python /app/manage.py runserver 0.0.0.0:8001