from django.views import generic
from django.core.urlresolvers import reverse
from django.contrib.auth import login
from django.shortcuts import redirect
from accounts import forms


class LoginView(generic.FormView):
    form_class = forms.AuthenticationForm
    success_url = 'accounts:user_profile_detail'
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        login(self.request, form.cleaned_data['user_authenticated'])
        url_to_redirect = reverse(self.success_url)
        return redirect(url_to_redirect)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            url_to_redirect = reverse(self.success_url)
            return redirect(url_to_redirect)
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
