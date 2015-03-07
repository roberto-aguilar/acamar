from django.views import generic


class ProfileView(generic.DetailView):
    template_name = 'common/user-detail.html'

    def get_object(self, queryset=None):
        return self.request.user
