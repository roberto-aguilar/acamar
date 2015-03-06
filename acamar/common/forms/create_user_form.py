from django import forms
from django.utils.translation import ugettext as _
from django.utils.translation import ugettext_lazy as __
from django.contrib.auth.models import User


class CreateUserForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput, label=__('Confirm password'))

    class Meta:
        model = User
        fields = ['username', 'password', 'confirm_password', 'first_name', 'last_name', 'email']
        labels = {
            'email': __('Email address')
        }
        widgets = {
            'password': forms.PasswordInput
        }

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True

    def clean(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password and confirm_password:
            if password != confirm_password:
                self.add_error('password', forms.ValidationError(
                    _('Passwords does not match'),
                    code='password_mismatch'

                ))
                self.add_error('confirm_password', forms.ValidationError(
                    _('Passwords does not match'),
                    code='password_mismatch'
                ))

        return self.cleaned_data
