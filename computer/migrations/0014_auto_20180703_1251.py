# Generated by Django 2.0.6 on 2018-07-03 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('computer', '0013_attendance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='student_data',
        ),
        migrations.DeleteModel(
            name='Attendance',
        ),
    ]
