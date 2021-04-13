from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Address


class EditAddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('streetNum', 'zipcode', 'state', 'city')


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image',)

class SignUp(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='')
    last_name = forms.CharField(max_length=30, required=True, help_text='Optional.')
    phoneNumber = forms.CharField(max_length=10, help_text='', required=True,
                                  widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    street_number = forms.CharField(max_length=20, help_text='', required=True,
                                    widget=forms.TextInput(attrs={'placeholder': 'Street Number'}))
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


from django.contrib.auth.models import User


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    first_name = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    # email = forms.CharField(label='', widget=forms.EmailInput(attrs={'placeholder', 'johndoe@example.com'}))
    email = forms.CharField(label='', max_length=100,
                            widget=forms.EmailInput
                            (attrs={'placeholder': 'Enter your email'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), required=True)
    password2 = forms.CharField(label='',
                                widget=forms.PasswordInput(attrs={'placeholder': 'Verify Password'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('streetNum', 'zipcode', 'city', 'state')
