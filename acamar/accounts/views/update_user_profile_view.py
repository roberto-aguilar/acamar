from django.views import generic
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from accounts import forms
from accounts.mixins import LoginRequiredMixin
from common.mixins import MessagesMixin


class UpdateUserProfileView(LoginRequiredMixin, MessagesMixin, generic.CreateView):
    template_name = 'accounts/update_user_profile.html'
    form_class = forms.UpdateUserProfileForm
    success_message = _('User profile successfully updated')
    error_message = _('An error ocurred trying to update the user profile')

    def get_success_url(self):
        return reverse('accounts:user_profile_detail')

    def get_form_kwargs(self):
        kwargs = super(UpdateUserProfileView, self).get_form_kwargs()
        kwargs.update({
            'instance': self.request.user
        })
        return kwargs
