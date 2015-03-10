from django.views import generic


class UserProfileDetailView(generic.DetailView):
    template_name = 'accounts/user_profile_detail.html'

    def get_object(self, queryset=None):
        return self.request.user
