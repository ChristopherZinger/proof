from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views


app_name = 'accounts'

urlpatterns = [
    url(r'^register/', views.register, name='register'),
    #url(r'^login/$', auth_views.LoginView.as_view(template_name='accounts/login.html')),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^login/', views.user_login, name='login'),
    url(r'^logout/', views.user_logout, name='logout'),
    # url(r'^dashboard/', views.dashboard, name='dashboard'),
    # url(r'^signup/$', core_views.signup, name='register'),

]
