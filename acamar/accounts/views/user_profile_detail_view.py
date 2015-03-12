from django.views import generic
from accounts.mixins import LoginRequiredMixin


class UserProfileDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'accounts/detail_user_profile.html'

    def get_object(self, queryset=None):
        return self.request.user
