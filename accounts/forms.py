from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from accounts.models import AuthorProfile


class UserForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        # fields = ['username', 'email']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = AuthorProfile
        fields = ['gender', 'date_of_birth', 'contact_number']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'class': 'datepicker',
                                                    'placeholder': 'yyyy-dd-mm'})
        }


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = AuthorProfile
        fields = ['image', 'contact_number', 'address']