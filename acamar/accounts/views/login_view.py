from django.views import generic
from django.core.urlresolvers import reverse
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from accounts import forms
from common import mixins


class LoginView(mixins.MessagesMixin, generic.FormView):
    form_class = forms.AuthenticationForm
    template_name = 'accounts/login.html'
    success_message = 'Login successful'
    error_message = 'Error trying to login, please try again'

    def __init__(self, **kwargs):
        self.success_url = reverse('accounts:user_profile_detail')

    def form_valid(self, form):
        login(self.request, form.cleaned_data['user_authenticated'])
        return super(LoginView, self).form_valid(form)

    def get_success_url(self):
        success_url = super(LoginView, self).get_success_url()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            next_url = form.cleaned_data['next_url']
            if next_url:
                return next_url
        return success_url

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(self.get_success_url())
        else:
            form_class = self.get_form_class()
            form = self.get_form(form_class)
            return self.render_to_response(self.get_context_data(form=form))

    def get_initial(self):
        initial = super(LoginView, self).get_initial()
        next_url = self.request.GET.get('next')
        initial = {
            'next_url': next_url
        }
        return initial
