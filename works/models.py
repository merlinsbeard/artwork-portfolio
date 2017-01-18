from django.db import models


class Work(models.Model):
    name = models.CharField(max_length=200)
    short_description = models.CharField(max_length=300, blank=False)
    description = models.TextField(blank=False)
    slug = models.SlugField()
    link = models.URLField()
    image = models.ImageField()
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class WorkImage(models.Model):
    name = models.ForeignKey(Work)
    image = models.ImageField()
    description = models.TextField()

    def __str__(self):
        return self.name.name + str(self.pk)


class WorkTechnology(models.Model):
    work = models.ForeignKey(Work)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.work.name + self.name
