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

TODO
-----
- [ ] Login/logout Link in the layout
- [ ] Inline forms for work details
- [ ] API POST, DELETE, and PUT 
