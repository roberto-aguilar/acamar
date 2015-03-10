from django.conf.urls import patterns, url
from django.utils.translation import ugettext_lazy as _
from common import views


urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(_(r'^language/$'), views.LanguageView.as_view(), name='language'),
    url(_(r'^accounts/login/$'), views.LoginView.as_view(), name='login'),
    url(_(r'^accounts/logout/$'), views.LogoutView.as_view(), name='logout'),
)
