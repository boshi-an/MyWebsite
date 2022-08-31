# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
RUN apt-get update && apt-get install -y iputils-ping
COPY . /code/
RUN rm -r /code/MyWebsite/Publications/migrations
RUN rm -r /code/MyWebsite/SiteView/migrations
RUN rm -r /code/MyWebsite/data
RUN python /code/MyWebsite/manage.py makemigrations --empty SiteView
RUN python /code/MyWebsite/manage.py makemigrations --empty Publications
RUN python /code/MyWebsite/manage.py makemigrations
RUN python /code/MyWebsite/manage.py migrate