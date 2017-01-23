from django.db import models
from django.contrib.auth.models import User
import datetime


class Me(models.Model):
    user = models.OneToOneField(User)
    short_description = models.CharField(max_length=300)
    long_description = models.TextField()
    image = models.ImageField()
    phone = models.CharField(max_length=40)

    def __str__(self):
        return self.user.first_name + self.user.last_name

    def full_name(self):
        full_name = "{} {}".format(
                self.user.first_name, self.user.last_name)
        return full_name


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
