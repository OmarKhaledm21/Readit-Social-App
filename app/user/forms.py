from django import forms

class SignupForm(forms.Form):
    username = forms.CharField(max_length=40, required=True)
    password = forms.CharField(max_length=200,required=True)
    retype_password = forms.CharField(max_length=200,required=True,label="Retype Password")
    first_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=False)
    email = forms.CharField(max_length=40, required=True)
    gender = forms.CharField(max_length=40, required=True)
    phone = forms.CharField(max_length=40, required=False, label="Phone number")

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form_style'


class SigninForm(forms.Form):
    username = forms.CharField(max_length=40, required=True)
    password = forms.CharField(max_length=200,required=True)

    def __init__(self, *args, **kwargs):
        super(SigninForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form_style'



    