# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
RUN apt-get update && apt-get install -y iputils-ping
COPY . /code/
RUN rm -rf /code/Publications/migrations
RUN rm -rf /code/SiteView/migrations
# RUN python /code/manage.py makemigrations --empty SiteView
# RUN python /code/manage.py makemigrations --empty Publications
# RUN python /code/manage.py makemigrations