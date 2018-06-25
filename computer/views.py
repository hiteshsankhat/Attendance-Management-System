from django.shortcuts import render
from . import forms
from . import models

# Create your views here.
def home_page(request):
    return render(request, "computer/home.html")

def student_login(request):
    form = forms.StudentLoginForm(request.POST or None)
    context ={
        'form':form,
        'user':"",
    }
    stud = models.Student
    if form.is_valid():
        username = form.cleaned_data.get('Username')
        Password = form.cleaned_data.get('Password')
        user = stud.objects.filter(roll_id__iexact=username)[0]
        context['user'] = user.first_name + " " + user.last_name
        return render(request, 'computer/student_login.html',context)
    return render(request, 'computer/student_login.html',context)

def staff_login(request):
    form = forms.StaffLoginForm(request.POST or None)
    context ={
        'form':form,
        'user':"",
    }
    stud = models.Staff
    if form.is_valid():
        username = form.cleaned_data.get('Username')
        Password = form.cleaned_data.get('Password')
        user = stud.objects.filter(roll_id__iexact=username)[0]
        context['user'] = user.first_name + " " + user.last_name
        return render(request, 'computer/Staff_login.html',context)
    return render(request, 'computer/staff_login.html',context)

def admin_login(request):
    return render(request, 'computer/admin_login.html')
