from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import UserProfile


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=False)
    role = forms.ChoiceField(choices=UserProfile.Role.choices)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'role', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email', '')

        if commit:
            user.save()
            # Signal creates profile; set selected role after save.
            user.profile.role = self.cleaned_data['role']
            user.profile.save()

        return user
