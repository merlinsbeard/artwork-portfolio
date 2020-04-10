from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView
from works import views, urls
from rest_framework import routers


urlpatterns = [
    url(r'^private/a/', admin.site.urls),
    url(r'^works/', include('works.urls', namespace='work')),
    url(r'^$', views.IndexView.as_view(), name='home'),
    url(r'^me/', include('contact.urls', namespace='contact')),
    url(r'^private/api-admin/', include('rest_framework.urls', namespace='rest_framework')),
    url('^', include('django.contrib.auth.urls')),

    url(r'^api/', include('clever_red.api')),
]
