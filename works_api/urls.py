from django.conf.urls import url, include
from rest_framework import routers
from . import views

app_name = "works_api"

router = routers.DefaultRouter()
router.register(r'works', views.WorkViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
   # url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
]
