from django.views import generic
from django.contrib.auth import logout


class LogoutView(generic.RedirectView):
    permanent = False
    pattern_name = 'common:index'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated():
            logout(self.request)
        return super(LogoutView, self).get(request, *args, **kwargs)
