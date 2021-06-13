FROM docker.io/python:3.9-slim-buster
LABEL maintainer="ottenwbe.public@gmail.com"

ADD analyzer/ /app/analyzer/
ADD requirements.txt /app

RUN pip install -r /app/requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

WORKDIR /app

ENV FLASK_ENV=prod
ENV FLASK_APP="analyzer"

ENTRYPOINT ["flask", "run", "--host", "0.0.0.0"]