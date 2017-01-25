from django.db import models
from django.utils.text import slugify


class Work(models.Model):
    name = models.CharField(max_length=200)
    short_description = models.CharField(max_length=300, blank=False)
    description = models.TextField(blank=False)
    slug = models.SlugField(unique=True)
    link = models.URLField()
    image = models.ImageField()
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.slug)
        super(Work, self).save(*args, **kwargs)


class WorkImage(models.Model):
    name = models.ForeignKey(Work, related_name='images')
    image = models.ImageField()
    description = models.TextField()

    def __str__(self):
        return self.name.name + str(self.pk)


class WorkTechnology(models.Model):
    work = models.ForeignKey(Work, related_name='techs')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        # return self.work.name + self.name
        return self.name
