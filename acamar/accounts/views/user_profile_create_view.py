from django.views import generic
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _
from accounts import forms
from common import mixins


class UserProfileCreateView(mixins.MessagesMixin, generic.CreateView):
    template_name = 'accounts/create_user_profile.html'
    form_class = forms.UserProfileCreateForm
    success_message = _('User profile created successfully')
    error_message = _('There was an error trying to create user profile')

    def get_success_url(self):
        return reverse('accounts:login')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            detail_user_profile_url = reverse('accounts:detail_user_profile')
            return redirect(detail_user_profile_url)
        else:
            return super(UserProfileCreateView, self).get(
                request, *args, **kwargs)
