from django.views import generic
from django.core.exceptions import ImproperlyConfigured
from django.contrib import messages


class MessagesMixin(generic.FormView):

    success_message = None
    error_message = None

    def form_valid(self, form):
        if self.success_message:
            messages.add_message(self.request, messages.SUCCESS, self.success_message)
        else:
            raise ImproperlyConfigured(
                'MessagesMixin form_valid require "self.success_message" to be defined')
        return super(MessagesMixin, self).form_valid(form)

    def form_invalid(self, form):
        if self.error_message:
            messages.add_message(self.request, messages.ERROR, self.error_message)
        else:
            raise ImproperlyConfigured(
                'MessagesMixin form_invalid require "self.error_message" to be defined')
        return super(MessagesMixin, self).form_invalid(form)
