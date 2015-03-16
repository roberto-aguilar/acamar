from django.views import generic
from accounts import mixins, models


class UserProfileDetailView(mixins.LoginRequiredMixin, generic.DetailView):
    template_name = 'accounts/detail_user_profile.html'
    context_object_name = 'user_profile'

    def get_object(self, queryset=None):
        authentication_user = self.request.user
        return models.UserProfile.objects.get(
            authentication_user=authentication_user
            )
