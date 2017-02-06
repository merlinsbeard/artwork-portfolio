from django.conf.urls import url
from . import views


app_name = 'works'

urlpatterns = [
    # /
    # /works/
    url(r'^$', views.IndexView.as_view(), name='list'),
    url(r'^add/', views.WorkCreateView.as_view(), name='add'),
    url(r'^(?P<slug>[-\w]+)/$',
        views.WorkDetailView.as_view(), name='detail'),
    url(r'^(?P<slug>[-\w]+)/update/$',
        views.WorkUpdateView.as_view(), name='update'),
]
