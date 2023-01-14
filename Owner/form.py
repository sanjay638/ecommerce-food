from django import forms

from Owner.models import AdminModel, Adminregister_Model


class AdminForm(forms.ModelForm):
    class Meta:
        model = AdminModel
        fields = ('Productname','Productid','Quality','uploadimage','gram','Description','amount',)



class Adminregister_Form(forms.ModelForm):
    class Meta:
        model = Adminregister_Model
        fields = ('adminid','name','email','password', 'phoneno', 'address', 'dob')