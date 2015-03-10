from django.conf.urls import patterns, url
from django.utils.translation import ugettext_lazy as _
from common import views


urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(_(r'^language/$'), views.LanguageView.as_view(), name='language'),
)
