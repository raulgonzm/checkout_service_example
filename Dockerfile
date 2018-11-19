FROM python:3.6
ARG ENV=local

# Initialize
RUN mkdir /code
WORKDIR /code

RUN mkdir /requirements
COPY ./requirements /requirements

COPY ./checkouts /app

RUN pip install -r /requirements/$ENV.txt

