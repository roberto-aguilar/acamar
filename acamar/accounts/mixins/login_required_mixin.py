from django.views import generic
from django.contrib.auth.views import redirect_to_login


class LoginRequiredMixin(generic.View):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect_to_login(next=request.get_full_path())
        return super(LoginRequiredMixin, self).dispatch(
            request, *args, **kwargs)
