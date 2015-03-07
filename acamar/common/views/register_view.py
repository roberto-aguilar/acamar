from django.views import generic
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from common import forms


class RegisterView(generic.CreateView):
    model = User
    template_name = 'common/register.html'
    form_class = forms.CreateUserForm

    def get_success_url(self):
        return reverse('common:login')
