# Generated by Django 5.1.1 on 2024-10-30 14:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('programs', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_code', models.CharField(max_length=100)),
                ('subject_name', models.CharField(max_length=100)),
                ('program', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subject_programs', to='MS.program')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_employee_ID', models.CharField(max_length=100)),
                ('teacher_first_name', models.CharField(max_length=100)),
                ('teacher_last_name', models.CharField(max_length=100)),
                ('teacher_email', models.EmailField(max_length=254)),
                ('program', models.ManyToManyField(related_name='teacher_programs', to='MS.program')),
                ('subject', models.ManyToManyField(related_name='teacher_subjects', to='MS.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=100)),
                ('student_first_name', models.CharField(max_length=100)),
                ('student_last_name', models.CharField(max_length=100)),
                ('student_email', models.EmailField(max_length=254)),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_programs', to='MS.program')),
                ('subject', models.ManyToManyField(related_name='student_subjects', to='MS.subject')),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_teachers', to='MS.teacher')),
            ],
        ),
    ]
