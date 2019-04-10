from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template import loader
from django.utils.translation import ugettext_lazy as _



class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta: 
        model = User
        fields = {
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2'
        }

    def save(self, commit=True):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user = super(RegistrationForm, self).save(commit=False)

        if commit:
            user.save()

        return user

    class EditProfileForm(UserChangeForm):

        class Meta:
            model =User
            fields = {
                'email',
                'first_name',
                'last_name'
            }

    class ContactForm(forms.Form):
        subject = forms.CharField(required=True)
        from_email = forms.EmailField(required=True)
        message = forms.CharField(widget=forms.Textarea)


    