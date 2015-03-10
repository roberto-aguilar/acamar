from django.views import generic
from django.core.urlresolvers import reverse
from accounts import models
from accounts import forms


class CreateUserProfileView(generic.CreateView):
    model = models.UserProfile
    template_name = 'accounts/create-user-profile.html'
    form_class = forms.CreateUserProfileForm

    def get_success_url(self):
        return reverse('accounts:login')
