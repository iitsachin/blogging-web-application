from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import profile


# in user creation form there are only three fields username,p1,p2 but we also want email
# so we make new form and inherit the UserCreation form and add email to it

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class meta:
        model = User
        fields = ['username', 'email', 'password1', 'passwoard2']

    # to save the email detail to user
    # imp without this email and other data will not be saved
    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class UserUpdate(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdate(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['image']
