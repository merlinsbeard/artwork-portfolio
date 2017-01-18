"""clever_red URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView, TemplateView
from django.core.urlresolvers import reverse_lazy

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^works/', include('works.urls', namespace='work')),
    #url(r'^', include('works.urls',)),
    url(r'^$', RedirectView.as_view(pattern_name='work:list'), name='home'),
    url(r'^me/$', TemplateView.as_view(template_name="me.html"), name='me'),
]
