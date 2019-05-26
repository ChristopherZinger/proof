from django.conf.urls import url
from . import views

app_name = 'projects'

urlpatterns = [
    url(r'^detail/(?P<id>\d+)/$', views.projectDetailView, name='detail'),
]
