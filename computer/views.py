from django.shortcuts import render, redirect
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
    if request.method == "POST":
        print(request.POST)
        if request.POST.get('take_attendance') is not None:
            return redirect("/take-attendance")
        elif request.POST.get('check_attendance') is not None:
            return redirect("/check-attendance")
        elif form.is_valid():
            username = form.cleaned_data.get('Username')
            Password = form.cleaned_data.get('Password')
            user = stud.objects.filter(roll_id__iexact=username)[0]
            context['user'] = user.first_name + " " + user.last_name
            return render(request, 'computer/staff_login.html', context)
    return render(request, 'computer/staff_login.html',context)

def admin_login(request):
    return render(request, 'computer/admin_login.html')

def check_attendance(request):
    return render(request, 'computer/check_attendance.html')


def take_attendance(request):
    attend = forms.TakeAttendance(request.POST or None)
    context = {
        'form':attend,
    }
    stud = models.Student
    subject_model = models.Subject
    if (request.POST.get('data') is not None):
        atten_model = models.Attendance()
        key = list(request.POST.keys())[1:-1]
        sub_name = request.POST.get('data').split(",")
        for k in key:
            add = models.Attendance(lec_count=sub_name[1],subject_data=sub_name[0],student_data=k)
            add.save()
    if attend.is_valid():
        data = attend.cleaned_data
        sem = data['semester']
        div = data['division']
        res = stud.objects.filter(semister__iexact=sem,division__iexact=div)
        context = {
            'data':data['subject'] + ","+ data['lecture_count'],
            'res':res,
        }
        return render(request, 'computer/add_attendance.html', context)
    return render(request, 'computer/take_attendance.html', context)
