Artwork
====

Contains the source code for my [portfolio
website](https://benray.dailywarrior.ph). Uses Django as the primary framework.
Still work in progress

Features
--------
* Single User authentication for the primary User
* EMAIL notification for contact us
* Forms for updating works and details
* localenv and prodenv for environment variables
* Gunicorn for deployment
* Django 1.10
* Materialize.css for user interface

Installation
----------
Install pip and virtualenv
```
$ sudo apt-get install python3-pip
$ sudo pip3 install virtualenv
```
Create a virtualenv
```
$ virtualenv -p /usr/bin/python3 venv
$ source venv/bin/activate
```

Clone the repo and install requirements
```
$ git clone git@github.com:merlinsbeard/artwork-portfolio.git
$ cd artwork-portfolio
$ pip install -r requirements.txt
```

**We will run a local development version**

Edit the .localenv for the settings
`$ vim .localenv`
Information about env can be found here
[django-envron](http://django-environ.readthedocs.io/en/latest/)

Migrate Database and create superuser
```
$ python manage.py migrate --settings=clever_red.settings 
$ python manage.py createsuperuser --settings=clever_red.settings
```

Run django
` python manage.py runserver --settings=clever_red.settings.local 0.0.0.0:8002
`
![](http://i.imgur.com/50Ooait.png)

**Create a single user this will act as the only user for the project one time
setup**
go to the admin page of django
`http://localhost:8002/admin/login/?next=/admin/`
Click + Add under the contact/Mes tab
![](http://i.imgur.com/Ro2RWYj.jpg)
* User field should point to the single user
* **Slug should always be** `me`
* Long description can accept markdown

After clicking save go back to the home page it will now show the details.
To edit the extra details just go to 
`http://localhost:8002/me/update`

**To add Works**
Go back to the admin page
` http://localhost:8002/admin/ `
Click on add works. After saving the works will show up in the front page. They
can be edited while login

**For Production**
Copy .localenv to .prodenv and fill the proper environment variables

Gunicorn
` $ gunicorn --bind 0.0.0.0:8000 clever_red.wsgi:application `

Docker

1. Create docker image first  
```bash
$ git clone https://github.com/merlinsbeard/artwork-portfolio.git
$ cd artwork-portfolio
$ docker build -t artwork:latest .
```

2. Update .prod.env for configurations  

```bash
$ vim .prod.env

EMAIL_URL=smtp://user@user.ph:password@smtp.localhost.com:587
EMAIL_TO='my_email@gmail.com'
SECRET_KEY='i!04_!5#_i=k$8s03-l06'

```

3. Create Docker Database

```bash
# Create Docker network first
$ docker network create --driver bridge artwork
# Create database
$ docker run --name artwork_db \
> --network artwork \
> --env POSTGRES_DB=artwork \
> -d postgres:latest
```

4. Run Container with environment variables

```bash
$ docker run --name artwork \
> --network artwork \
> --env DB_HOST=artwork_db \
> --env DROPBOX_OAUTH2_TOKEN=my-token \
> -p 8000:8000 \
> -v $PWD/.prodenv:/artwork/.prodenv \
> -d artwork:latest
```

5. Migrate Database and create superuser

```bash
$ docker exec -it artwork python manage.py migrate
$ docker exec -it artwork python manage.py createsuperuer
```

6. Check browser and open in `localhost:8000`


## Environment Variables

| Name | Description |
|------|-------------|
| DB_HOST | url of database |
| DB_NAME | Database name |
| DB_USER | Database Username |
| DB_PASSWORD | Database Password |
| DB_PORT | Database Port |
| GS_BUCKET_NAME |  Google storage bucket name |
| GOOGLE_APPLICATION_CREDENTIALS | Path to service account JSON keyfile [see more](https://cloud.google.com/storage/docs/authentication#generating-a-private-key)
