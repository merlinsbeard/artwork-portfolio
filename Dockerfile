FROM python:onbuild

WORKDIR .

EXPOSE 8000:8000

CMD python manage.py runserver --settings=clever_red.settings.prod
