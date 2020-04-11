from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.conf import settings


class Work(models.Model):
    name = models.CharField(max_length=200)
    short_description = models.CharField(max_length=300, blank=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True)
    link = models.URLField(blank=True)
    image = models.ImageField(upload_to="work-banner", blank=True)
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('work:detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Work, self).save(*args, **kwargs)

    @property
    def image_append(self):
        image = self.image
        if settings.DEFAULT_FILE_STORAGE == 'storages.backends.gcloud.GoogleCloudStorage':
            return f"{settings.GS_URL}{image.name}"
        return image.url


class WorkImage(models.Model):
    name = models.ForeignKey(Work, related_name='images',
            on_delete=models.CASCADE)
    image = models.ImageField()
    description = models.TextField()

    def __str__(self):
        return self.name.name + str(self.pk)

    @property
    def image_append(self):
        image = self.image
        if settings.DEFAULT_FILE_STORAGE == 'storages.backends.gcloud.GoogleCloudStorage':
            return f"{settings.GS_URL}{image.name}"
        return image.url


class WorkTechnology(models.Model):
    work = models.ForeignKey(Work, related_name='techs', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
