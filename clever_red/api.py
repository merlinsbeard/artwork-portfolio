from django.conf.urls import include, url
from contact.views import MeApiView


urlpatterns = [
    url(r'^', include('works_api.urls', namespace='work-api')),
    url(r'^me/$', MeApiView.as_view(), name='meapi')
]
