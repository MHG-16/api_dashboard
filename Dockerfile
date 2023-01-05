# Pick a low configuration python base image
FROM python:3.7.16-slim-bullseye

#set working directory
WORKDIR /usr/src/app

#Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
#Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1
#  Expose the port 5000 of the docker container
EXPOSE 5000


COPY requirements.txt .

# Install required dependencies
RUN apt-get update
RUN apt-get -y install build-essential libffi-dev python-dev
RUN apt-get install  libmariadb-dev -y

# Install all the requirements
COPY ./requirements.txt /usr/src/app/
RUN pip3 install -r requirements.txt

# Copy all the flask project files into the WORKDIR
COPY . /usr/src/app/

CMD python manage.py

EXPOSE 5000
