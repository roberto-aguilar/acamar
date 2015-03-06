from django.views import generic


class LanguageView(generic.TemplateView):
    template_name = 'common/language.html'

    def get_context_data(self, *args, **kwargs):
        context = super(LanguageView, self).get_context_data(**kwargs)
        context['redirect_to'] = self.request.META.get('HTTP_REFERER')
        return context
