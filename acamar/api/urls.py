from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken import views as authtoken_views
from api.views import users_view

router = routers.DefaultRouter()
router.register(r'users', users_view.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', authtoken_views.obtain_auth_token),
]
