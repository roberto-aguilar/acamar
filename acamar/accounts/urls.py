from django.conf.urls import patterns, url
from django.utils.translation import ugettext_lazy as _
from accounts import views


urlpatterns = patterns('',
    url(_(r'^register/$'), views.CreateUserProfileView.as_view(), name='register'),
)
