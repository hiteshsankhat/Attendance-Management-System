# Generated by Django 2.0.6 on 2018-07-03 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computer', '0010_auto_20180703_1237'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lec_count', models.IntegerField()),
                ('student_data', models.ManyToManyField(to='computer.Student')),
                ('subject_data', models.ManyToManyField(to='computer.Subject')),
            ],
        ),
    ]
