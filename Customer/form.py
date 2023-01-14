from django import forms

from Customer.models import UserRegistration


class RegisterForm(forms.ModelForm):
    dob = forms.DateField( widget=forms.SelectDateWidget)

    class Meta:
        model = UserRegistration
        fields = ('firstname','email','password','mobilenumber','dob','gender','address')


