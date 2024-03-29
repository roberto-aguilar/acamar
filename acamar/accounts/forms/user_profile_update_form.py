from django import forms
from django.utils.translation import ugettext_lazy
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from accounts.models import UserProfile


class UserProfileUpdateForm(forms.ModelForm):
    image = forms.ImageField(
        required=False, label=ugettext_lazy('Profile image')
        )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'image']
        labels = {
            'email': ugettext_lazy('Email address')
        }

    def __init__(self, *args, **kwargs):
        super(UserProfileUpdateForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True
        try:
            user_profile = UserProfile.objects.get(
                authentication_user=kwargs['instance']
                )
        except UserProfile.DoesNotExist:
            raise ValidationError(
                'The username "%(username)s" does not have a related UserProfile',
                code='invalid_username',
                params={
                    'username': kwargs['instance'].username
                }
                )
        self.initial.update({
            'image': user_profile.image
        })

    def save(self, commit=True):
        user = super(UserProfileUpdateForm, self).save(commit=False)
        user_profile = UserProfile.objects.get(authentication_user=user)
        user_profile.image = self.cleaned_data['image']
        if commit:
            user_profile.save()
            user.save()
        return user
