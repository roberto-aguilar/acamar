from django.views import generic
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from accounts import forms
from accounts.mixins import LoginRequiredMixin
from common.mixins import MessagesMixin


class UserProfileUpdateView(LoginRequiredMixin, MessagesMixin, generic.CreateView):
    template_name = 'accounts/update_user_profile.html'
    form_class = forms.UserProfileUpdateForm
    success_message = _('User profile successfully updated')
    error_message = _('An error ocurred trying to update the user profile')

    def get_success_url(self):
        return reverse('accounts:detail_user_profile')

    def get_form_kwargs(self):
        kwargs = super(UserProfileUpdateView, self).get_form_kwargs()
        kwargs.update({
            'instance': self.request.user
        })
        return kwargs
