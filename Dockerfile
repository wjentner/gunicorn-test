FROM python:3.9-slim

COPY ./* .

RUN pip install -r requirements.txt

CMD gunicorn --config gunicorn.conf.py app:app