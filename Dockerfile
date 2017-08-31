FROM python:3.6.1-onbuild
ADD . /artwork
COPY ./entrypoint.sh /artwork/
WORKDIR /artwork
# Add Environment Variables here
ENV DJANGO_SETTINGS_MODULE="clever_red.settings.prod"
EXPOSE 8000
RUN pip install --no-cache-dir -r requirements.txt
RUN ["chmod", "+x", "/artwork/entrypoint.sh"]
ENTRYPOINT ["sh", "/artwork/entrypoint.sh"]
