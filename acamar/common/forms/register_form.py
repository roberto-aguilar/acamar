from django import forms
from django.utils.translation import ugettext, ugettext_lazy
from django.contrib.auth.models import User
from common import validators


class CreateUserForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput, label=ugettext_lazy('Confirm password'))

    class Meta:
        model = User
        fields = ['username', 'password', 'confirm_password', 'first_name', 'last_name', 'email']
        labels = {
            'email': ugettext_lazy('Email address')
        }
        widgets = {
            'password': forms.PasswordInput
        }

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].validators.append(validators.validate_username_does_not_exist)
        self.fields['username'].help_text = ''
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True

    def clean(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password and confirm_password:
            if password != confirm_password:
                self.add_error('password', forms.ValidationError(
                    ugettext('Passwords does not match'),
                    code='password_mismatch'

                ))
                self.add_error('confirm_password', forms.ValidationError(
                    ugettext('Passwords does not match'),
                    code='password_mismatch'
                ))

        return self.cleaned_data

    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
