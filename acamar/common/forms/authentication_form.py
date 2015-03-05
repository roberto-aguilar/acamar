# -*- coding: utf8 -*-
from django import forms
from django.contrib.auth import authenticate
from common.validators import authentication_validators


class AuthenticationForm(forms.Form):
    username = forms.CharField(max_length=30, label='Usuario', error_messages={
        'required': 'Este campo es requerido'
    }, validators=[authentication_validators.validate_user_exists, authentication_validators.validate_user_is_active])
    password = forms.CharField(max_length=128, label='Password', error_messages={
        'required': 'Este campo es requerido'
    }, widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user_authenticated = authenticate(username=username, password=password)
            if user_authenticated is None:
                self.add_error('password', forms.ValidationError(
                    'Contraseña incorrecta',
                    code='invalid_password'
                ))
            else:
                self.cleaned_data['user_authenticated'] = user_authenticated

        return self.cleaned_data
