from django.views import generic
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from accounts import models, forms
from common import mixins


class CreateUserProfileView(mixins.MessagesMixin, generic.CreateView):
    model = models.UserProfile
    template_name = 'accounts/create_user_profile.html'
    form_class = forms.CreateUserProfileForm
    success_message = _('User profile created successfully')
    error_message = _('There was an error trying to create user profile')

    def get_success_url(self):
        return reverse('accounts:login')
