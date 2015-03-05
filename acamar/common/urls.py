from django.conf.urls import patterns, url
from common.views import index_view, login_view, logout_view, register_view


urlpatterns = patterns('',
    url(r'^$', index_view.IndexView.as_view(), name='index'),
    url(r'^accounts/login/$', login_view.LoginView.as_view(), name='login'),
    url(r'^accounts/logout/$', logout_view.LogoutView.as_view(), name='logout'),
    url(r'^accounts/register/$', register_view.RegisterView.as_view(), name='register'),
)
