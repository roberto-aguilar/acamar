from django.views.generic import UpdateView
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from accounts import forms
from accounts.mixins import LoginRequiredMixin
from common.mixins import MessagesMixin


class UserProfileUpdateView(LoginRequiredMixin, MessagesMixin, UpdateView):
    template_name = 'accounts/update_user_profile.html'
    form_class = forms.UserProfileUpdateForm
    success_message = _('User profile successfully updated')
    error_message = _('An error ocurred trying to update the user profile')

    def get_success_url(self):
        return reverse('accounts:detail_user_profile')

    def get_object(self):
        return self.request.user
