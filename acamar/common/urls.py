from django.conf.urls import patterns, include, url
from django.contrib import admin
from common import views

urlpatterns = patterns('',
    url(r'^$', views.IndexTemplateView.as_view(), name='index'),
)
