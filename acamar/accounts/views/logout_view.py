from django.views import generic
from django.contrib.auth import logout
from django.contrib import messages
from django.utils.translation import ugettext as _


class LogoutView(generic.RedirectView):
    permanent = False
    pattern_name = 'common:index'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated():
            logout(self.request)
            messages.add_message(
                request=request, level=messages.SUCCESS,
                message=_('Logout successful'))
        else:
            messages.add_message(
                request=request, level=messages.ERROR,
                message=_('There is no user logged in'))
        return super(LogoutView, self).get(request, *args, **kwargs)
