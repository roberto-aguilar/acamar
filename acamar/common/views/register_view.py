from django.views import generic
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from common.forms import create_user_form

class RegisterView(generic.CreateView):
    model = User
    template_name = 'common/create_user.html'
    form_class = create_user_form.CreateUserForm

    def get_success_url(self):
        return reverse('common:index')
