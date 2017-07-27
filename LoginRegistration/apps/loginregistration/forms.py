from django import forms
from django.core.exceptions import ValidationError
from .models import User

class UsernameForm(forms.ModelForm):
    first_name = forms.CharField(min_length=2)
    last_name = forms.CharField(min_length=2)
    email = forms.CharField(min_length=8, max_length=25)
    confirm_password = forms.CharField(max_length=25,min_length=8,
            widget=forms.PasswordInput)
    password = forms.CharField(max_length=25,min_length=8,
            widget=forms.PasswordInput)

    def clean(self):
        cleaned = self.cleaned_data
        # Check for MAX length
        # if len(cleaned['username']) > 25:
        #     raise forms.ValidationError("username":"Username must be less than 26 characters.")
        # Check for Dup
        if len(User.objects.filter(email=cleaned['email'])) > 0:
            raise forms.ValidationError({"email":"Email already taken. Must be unique."})
        # Validate Passwd
        if cleaned['password'] != cleaned['confirm_password']:
            raise forms.ValidationError({"password":"Passwords do not match"})


    class Meta:
        model = User
        fields = ['first_name','last_name','email','password','confirm_password']

class LoginForm(forms.ModelForm):
    email = forms.CharField(min_length=8, max_length=25)
    password = forms.CharField(max_length=25,min_length=8,
            widget=forms.PasswordInput)

    def clean(self):
        cleaned = self.cleaned_data
        # Check for user
        result = User.objects.filter(email=cleaned['email'])
        print result
        if len(result) != 1:
            raise forms.ValidationError({"email":"User not found."})
        else:
            # Validate Passwd
            if cleaned['password'] != result[0]['password']:
                raise forms.ValidationError({"password":"Passwords do not match"})

    class Meta:
        model = User
        fields = ['email','password']

# Devon example
# class FunUserForm(forms.ModelForm):
#     first_name = forms.CharField(min_length=3)
#     confirm_password = forms.CharField(max_length=25,min_length=8,
#             widget=forms.PasswordInput)
#     password = forms.CharField(max_length=25,min_length=8,
#             widget=forms.PasswordInput)

#     def clean(self):
#         cleaned_data = super(FunUserForm, self).clean()
#         if cleaned_data('password') != cleaned_data('confirm'):
#             raise forms.ValidationError({"password":"Passwords do not match"})
#         # return cleaned_data

#     class Meta:
#         model = FunUser
#         fields = ['first_name', 'last_name']
