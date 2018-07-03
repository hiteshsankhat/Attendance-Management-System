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
        roll_id = user.roll_id
        sem = user.semister
        subject = models.Subject.objects.filter(semister=sem)
        d={}
        subject_name = []
        for j in subject:
            sub = j.abr
            subject_name.append(j.name)
            d[j.name] = 0
            attend = models.Attendance.objects.filter(subject_data=sub,student_data=roll_id)
            for a in attend:
                d[j.name]+=(a.lec_count)
        # vall = d.values()
        # context['nma'] = vall
        context['sub'] = d
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
    form = forms.CheckAttendance(request.POST or None)
    context = {
        'form':form,
    }
    if form.is_valid():
        sem = request.POST.get('semester')
        div = request.POST.get('division')
        subject = models.Subject.objects.filter(semister=sem)
        student = models.Student.objects.filter(division=div, semister=sem)
        student_name = []
        subject_name = []

        att = {}
        for i in student:
            d = {}
            roll_id = i.roll_id
            student_name.append([i.first_name + " "+i.last_name,roll_id])
            for j in subject:
                sub = j.abr
                if sub not in subject_name :
                    subject_name.append(sub)
                d[sub] = 0
                attend = models.Attendance.objects.filter(subject_data=sub,student_data=roll_id)
                for a in attend:
                    d[sub]+=(a.lec_count)
            att[roll_id] = d

        context = {
            'form':form,
            'student':student_name,
            'subject':subject_name,
            'attend':att
        }
        return render(request, 'computer/check_attendance.html',context)
    return render(request, 'computer/check_attendance.html',context)


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
