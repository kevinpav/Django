from django import forms
from django.core.exceptions import ValidationError
from .models import User

class UsernameForm(forms.ModelForm):
    username = forms.CharField(min_length=8, max_length=25)

    def clean(self):
        cleaned = self.cleaned_data
        # Check for MAX length
        if len(cleaned['username']) > 25:
            raise forms.ValidationError("Username must be less than 26 characters.")
        # Check for Dup
        if len(User.objects.filter(username=cleaned['username'])) > 0:
            raise forms.ValidationError("Username already taken. Must be unique.")

    class Meta:
        model = User
        fields = ['username']

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
