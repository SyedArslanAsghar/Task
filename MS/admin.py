from django.contrib import admin
from .models import Program, Subject, Teacher, Student

class AdminProgram(admin.ModelAdmin):
    list_display = ('id','programs', 'description','duration','eligibilityCriteria','creditHours')
    search_fields = ('programs',)


class AdminSubject(admin.ModelAdmin):
    list_display = ('subject_code', 'subject_name', 'program')
    search_fields = ('subject_code', 'subject_name')


class AdminTeacher(admin.ModelAdmin):
    list_display = (
        'teacher_employee_ID', 
        'teacher_first_name', 
        'teacher_last_name', 
        'teacher_email', 
        'get_programs', 
        'get_subjects'
    )
    search_fields = ('teacher_employee_ID', 'teacher_first_name', 'teacher_last_name')

    def get_programs(self, obj):
        return ", ".join([p.programs for p in obj.program.all()])
    get_programs.short_description = 'Programs'

    def get_subjects(self, obj):
        return ", ".join([s.subject_name for s in obj.subject.all()])
    get_subjects.short_description = 'Subjects'


class AdminStudent(admin.ModelAdmin):
    list_display = (
        'student_id', 
        'student_first_name', 
        'student_last_name', 
        'student_email', 
        'program', 
        'get_subjects', 
        'get_teacher'
    )
    search_fields = ('student_id', 'student_first_name', 'student_last_name', 'student_email')

    def get_subjects(self, obj):
        return ", ".join([s.subject_name for s in obj.subject.all()])
    get_subjects.short_description = 'Subjects'

    def get_teacher(self, obj):
        return obj.teacher if obj.teacher else "No Teacher Assigned"
    get_teacher.short_description = 'Teacher'


# Registering models
admin.site.register(Program, AdminProgram)
admin.site.register(Subject, AdminSubject)
admin.site.register(Teacher, AdminTeacher)
admin.site.register(Student, AdminStudent)
