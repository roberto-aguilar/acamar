from django.conf.urls import patterns, url
from django.utils.translation import ugettext_lazy as _
from accounts import views


urlpatterns = patterns('',
    url(_(r'^register/$'), views.UserProfileCreateView.as_view(), name='register'),
    url(_(r'^login/$'), views.LoginView.as_view(), name='login'),
    url(_(r'^logout/$'), views.LogoutView.as_view(), name='logout'),
    url(_(r'^profile/$'), views.UserProfileDetailView.as_view(), name='user_profile_detail'),
    url(_(r'^update-profile/$'), views.UpdateUserProfileView.as_view(), name='update_user_profile'),
)
