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
    semister = models.IntegerField(null=True)

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
    semister = models.IntegerField()

    def __str__(self):
        return self.first_name + self.last_name

class Attendance(models.Model):
    subject_data = models.CharField(max_length=8)
    lec_count = models.IntegerField()
    student_data = models.CharField(max_length=10)
