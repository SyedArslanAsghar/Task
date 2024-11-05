from django.db import models

class Program(models.Model):
    programs = models.CharField(max_length=100)
    description = models.TextField(null=True)
    duration = models.CharField(max_length=100, null=True)
    eligibilityCriteria = models.CharField(max_length=200 )
    creditHours = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.programs



class Subject(models.Model):
    subject_code = models.CharField(max_length=100)
    subject_name = models.CharField(max_length=100)
    program = models.ForeignKey(Program, null=True, on_delete=models.CASCADE, related_name='subject_programs')

    def __str__(self):
        return f"{self.subject_code} - {self.subject_name}"


class Teacher(models.Model):
    teacher_employee_ID = models.CharField(max_length=100)
    teacher_first_name = models.CharField(max_length=100)
    teacher_last_name = models.CharField(max_length=100)
    teacher_email = models.EmailField()
    program = models.ManyToManyField(Program, related_name='teacher_programs')
    subject = models.ManyToManyField(Subject, related_name='teacher_subjects')

    def __str__(self):
        return f"{self.teacher_first_name} {self.teacher_last_name}"


class Student(models.Model):
    student_id = models.CharField(max_length=100)
    student_first_name = models.CharField(max_length=100)
    student_last_name = models.CharField(max_length=100)
    student_email = models.EmailField()
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='student_programs')
    subject = models.ManyToManyField(Subject, related_name='student_subjects')
    teacher = models.ForeignKey(Teacher, null=True, on_delete=models.SET_NULL, related_name='student_teachers')

    def __str__(self):
        return f"{self.student_first_name} {self.student_last_name}"
    
    
