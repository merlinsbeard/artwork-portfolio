FROM python:3.6.3
LABEL maintainer="bjpaat@dailywarrior.ph"
COPY . /artwork
COPY ./entrypoint.sh /artwork/
WORKDIR /artwork
# Add Environment Variables here
ENV DJANGO_SETTINGS_MODULE="clever_red.settings.prod"
EXPOSE 8000
RUN ["pip", "install", "-U",  "pip"]
RUN ["pip" ,"install", "-U", "-r", "requirements.txt"]
RUN ["chmod", "+x", "/artwork/entrypoint.sh"]
ENTRYPOINT ["/artwork/entrypoint.sh"]
