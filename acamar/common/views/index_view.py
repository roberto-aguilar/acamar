from django.views import generic
from django.core.urlresolvers import reverse
from django.shortcuts import redirect


class IndexView(generic.TemplateView):
    template_name = 'common/index.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated():
            user_profile_detail_url = reverse('accounts:detail_user_profile')
            return redirect(user_profile_detail_url)
        else:
            return super(IndexView, self).get(request, *args, **kwargs)
