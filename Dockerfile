# Pull base image
FROM ubuntu:14.04

# OS Dependencies
RUN apt-get update --fix-missing && \
  apt-get upgrade -y

RUN apt-get install -y python \
  python-dev \
  python-pip \
  python-virtualenv \
  libffi-dev \
  libssl-dev \
  libxml2-dev \
  libxslt1-dev \
  libjpeg8-dev \
  zlib1g-dev \
  wget \
  unzip \
  build-essential \
  libssl-dev \
  libffi-dev

# Use an official Python runtime as a base image
FROM python:2.7


# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Copy the key for remote hosts in our docker container.
RUN cp key/*.pem /home/

# Make port 80 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME flaskapp

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements/requirements.txt

# Run app.py when the container launches
CMD ["python", "src/app.py"]

