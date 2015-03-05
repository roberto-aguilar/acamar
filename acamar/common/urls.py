from django.conf.urls import patterns, url
from common import views


urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^accounts/login/$', views.LoginView.as_view(), name='login'),
    url(r'^accounts/logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^accounts/register/$', views.RegisterView.as_view(), name='register'),
)
