from django.conf.urls import patterns, include, url, static
from django.conf import settings
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('api.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^', include('common.urls', namespace='common')),
    url(_(r'^accounts/'), include('accounts.urls', namespace='accounts')),
)

if settings.DEBUG:
    urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
