from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = "works_api"

router = routers.SimpleRouter()
router.register(r'works', views.WorkViewSet)

urlpatterns = format_suffix_patterns(router.urls)
