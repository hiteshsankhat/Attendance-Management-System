from django import forms

# class NameForm(forms.Form):
#     your_name = forms.CharField(label='Your name', max_length=100)


class StudentLoginForm(forms.Form):
    Username = forms.CharField(label='Username', max_length=80,
                widget=forms.TextInput(
                    attrs={
                        "class": "form-control",
                        "placeholder": "Username"
                        }
                    )
                )
    Password = forms.CharField(label='Password', max_length=80,
                widget=forms.PasswordInput(
                    attrs= {
                        'class':"form-control",
                        "placeholder": "Password"
                        }
                    )
                )

class StaffLoginForm(forms.Form):
    Username = forms.CharField(label='Username', max_length=80,
                widget=forms.TextInput(
                    attrs={
                        "class": "form-control",
                        "placeholder": "Username"
                        }
                    )
                )
    Password = forms.CharField(label='Password', max_length=80,
                widget=forms.PasswordInput(
                    attrs= {
                        'class':"form-control",
                        "placeholder": "Password"
                        }
                    )
                )
