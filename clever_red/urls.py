from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView, TemplateView
from django.core.urlresolvers import reverse_lazy
from works import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'works', views.WorkViewSet)
router.register(r'workstech',views.WorkTechViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^works/', include('works.urls', namespace='work')),
    #url(r'^', include('works.urls',)),
    url(r'^$', RedirectView.as_view(pattern_name='work:list'), name='home'),
    #url(r'^me/$', TemplateView.as_view(template_name="me.html"), name='me'),
    url(r'^me/', include('contact.urls', namespace='contact')),
    url(r'^work-api/', include(router.urls)),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),


]

