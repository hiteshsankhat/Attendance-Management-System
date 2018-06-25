from django.db import models

# Create your models here.
class Staff(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    roll_id = models.CharField(max_length=10)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name + self.last_name

class Subject(models.Model):
    name = models.CharField(max_length=80)
    abr = models.CharField(max_length=8)

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    middle_name = models.CharField(max_length=40)
    roll_id = models.CharField(max_length=10)
    division = models.CharField(max_length=2)
    batch = models.CharField(max_length=2)
    batch_id = models.IntegerField()

    def __str__(self):
        return self.first_name + self.last_name

class Attendance(models.Model):
    student_data = models.OneToOneField(Student,on_delete=models.CASCADE)
    sudject_data = models.OneToOneField(Subject,on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    lec_count = models.IntegerField()


class Semister_5(models.Model):
    students = models.ForeignKey(Student, on_delete=models.CASCADE)
    subjects = models.ForeignKey(Subject, on_delete=models.CASCADE)
    attendances = models.ForeignKey(Attendance, on_delete=models.CASCADE)