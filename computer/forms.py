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

semester_choice = (
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('6','6'),
    ('7','7'),
    ('8','8')
)

division_choice = (
    ('A','A'),
    ('B','B'),
    ('C','C'),
)

subject_choice = (
    ('ML','Manchine Learning'),
    ('DL','Deep Learning'),
    ('NPL','Natural Processing Language')
)

class TakeAttendance(forms.Form):
    semester = forms.ChoiceField(choices=semester_choice,label='Semester',
                widget=forms.Select(
                        attrs= {
                            'class':'form-control'
                        }
                    )
                )
    division = forms.ChoiceField(choices=division_choice,label='Division',
                widget=forms.Select(
                        attrs= {
                            'class':'form-control'
                        }
                    )
                )
    subject = forms.ChoiceField(choices=subject_choice,label='Subject',
                widget=forms.Select(
                        attrs= {
                            'class':'form-control'
                        }
                    )
                )
    lecture_count = forms.CharField(label="Lecture Count",max_length=80,
                widget=forms.TextInput(
                    attrs={
                        "class": "form-control",
                        "style": "padding=5px",
                        }
                    )
                )

class AddAttendance(forms.Form):
    check = forms.BooleanField(label='',required=False)


class CheckAttendance(forms.Form):
    semester = forms.ChoiceField(choices=semester_choice,label='Semester',
                widget=forms.Select(
                        attrs= {
                            'class':'form-control'
                        }
                    )
                )
    division = forms.ChoiceField(choices=division_choice,label='Division',
                widget=forms.Select(
                        attrs= {
                            'class':'form-control'
                        }
                    )
                )
