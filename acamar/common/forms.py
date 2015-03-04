from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class AuthenticationForm(forms.Form):
    username = forms.CharField(max_length=30, label='Usuario', error_messages={
        'required': 'Este campo es requerido'
    })
    password = forms.CharField(max_length=128, label='Password', error_messages={
        'required': 'Este campo es requerido'
    }, widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError(
                'No se encontro una cuenta asociada al usuario "%(username)s"',
                code='user_not_found',
                params={
                    'username': username
                }
            )
        if user.is_active is False:
            raise forms.ValidationError(
                'La cuenta asociada al usuario "%(username)s" se encuentra desactivada',
                code='user_not_active',
                params={
                    'username': username
                }
            )
        return username

    def clean_password(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError(
                    'Contrasena incorrecta',
                    code='incorrect_password'
                )
            else:
                self.user = user

        return self.cleaned_data

    def get_user(self):
        return self.user
