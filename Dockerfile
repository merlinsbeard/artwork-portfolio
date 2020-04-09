FROM python:3.6.3
LABEL maintainer="me@benpaat.xyz"

ENV PYTHONUNBUFFERED 1


WORKDIR /artwork
COPY requirements.txt /artwork/requirements.txt

RUN ["pip", "install", "-U",  "pip"]
RUN ["pip" ,"install", "-r", "requirements.txt"]

COPY . /artwork
COPY ./entrypoint.sh /artwork/

# Add Environment Variables here
ENV DJANGO_SETTINGS_MODULE="clever_red.settings.prod"
# Path of service_application.json from google
ENV GOOGLE_APPLICATION_CREDENTIALS="/secrets/secret.json"
ENV GUNICORN_WORKERS="4"

# Expose Port
EXPOSE 8000

# Turn entrypoint into executable
RUN ["chmod", "+x", "/artwork/entrypoint.sh"]
ENTRYPOINT ["/artwork/entrypoint.sh"]
