from django import forms
from django.contrib.auth import authenticate
from django.utils.translation import ugettext, ugettext_lazy
from accounts import validators


class AuthenticationForm(forms.Form):
    username = forms.CharField(max_length=30, validators=[validators.validate_user_exists,
        validators.validate_user_is_active], label=ugettext_lazy('Username'))
    password = forms.CharField(max_length=128, widget=forms.PasswordInput, label=ugettext_lazy('Password'))
    next_url = forms.CharField(max_length=128, required=False, widget=forms.HiddenInput)

    def is_valid(self):
        is_valid = super(AuthenticationForm, self).is_valid()
        if is_valid:
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            user_authenticated = authenticate(username=username, password=password)
            if user_authenticated is None:
                self.add_error('password', forms.ValidationError(
                    ugettext('Incorrect password'),
                    code='incorrect_password'
                ))
                is_valid = False
            else:
                self.cleaned_data['user_authenticated'] = user_authenticated
        return is_valid
