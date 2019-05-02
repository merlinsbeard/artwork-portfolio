from django.conf.urls import url
from . import views

app_name = "contact"

urlpatterns = [
        # /
        url(r'^$', views.IndexView.as_view(), name='me'),
        # /form

        url(r'^contact/$', views.contact, name='contact'),
        # /me/update
        url(r'^update/$', views.MeUpdateView.as_view(), name='update'),
        url(r'^api/$', views.MeApiView.as_view(), name='meapi')
]
