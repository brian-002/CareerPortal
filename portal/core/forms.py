from django import forms

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth.models import User

from .models import UserProfile, JobApplication



class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'enter your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':' enter your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2') 

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'enter your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder':' enter your email',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':' enter your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':' repeat your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'






class UserProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)  # Exclude the 'user' field since we don't want to allow changing it

    def __init__(self, *args, **kwargs):
        super(UserProfileEditForm, self).__init__(*args, **kwargs)
        # Customize form field attributes here if needed
        # For example, you can add placeholders or change labels:
        self.fields['profile_image'].widget.attrs.update({'class': 'custom-file-input'})




class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        exclude = ('user_profile', 'application_date')
