from django.shortcuts import redirect, render
from MS.models import Program, Teacher, Student, Subject


def AddPrograms(request):
    if request.method == 'POST':
        program_name = request.POST.get('program_name')
        description = request.POST.get('description')
        duration = request.POST.get('duration')
        criteria	 = request.POST.get('EligibilityCriteria')
        hours = request.POST.get('creditHours')
        if program_name:
            print(f"Received program_name: {program_name}")
            # Create the new program
            Program.objects.create(programs=program_name, description = description, duration = duration, eligibilityCriteria = criteria, creditHours = hours)

            # Redirect to the programs list after creation
            return redirect('pro')
    
    # Render the form if it’s a GET request or form is not valid
    return render(request, 'AddProgram.html')

def Programs(request):
    programs = Program.objects.all()
    return render(request, 'program.html', {'programs': programs})

def addSubjects(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        name = request.POST.get('name')
        program_ids = request.POST.get('program')
        if code and program_ids:
            programs = Program.objects.get(id=program_ids)
            Subject.objects.create(subject_code = code, subject_name = name, program = programs)
            # program = Program.objects.filter(id__in=program_ids)
            # Subject.program.set(program)
            # sub.program.set(program)
            print('-----------program post if running ------------')
            print(code, name, programs)
            return redirect('/Subjects/')

    # subjects_list = Subject.objects.all()
    programs_list = Program.objects.all()
    return render(request, 'AddSubject.html', {'programs': programs_list})

def Subjects_list(request):
    subjects_list = Subject.objects.all()
    print(subjects_list)
    return render(request, 'subject.html', {'subject': subjects_list})

def AddTeacher(request):
    if request.method == 'POST':
        Teacher_id = request.POST.get('employee_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        subjectsIDs = request.POST.getlist('subjects')
        programIDs = request.POST.getlist('program')
        print('subjectsIDs: ', type(subjectsIDs),'-----------------------',subjectsIDs)
        print('programIDs: ', type(programIDs),'-----------------------',programIDs)
        
        if Teacher_id and first_name and last_name and email:
            Te = Teacher.objects.create(teacher_employee_ID = Teacher_id,teacher_first_name = first_name, teacher_last_name = last_name, teacher_email = email)
            subjects = Subject.objects.filter(id__in=subjectsIDs)
            programms = Program.objects.filter(id__in=programIDs)
            print('subjects: ', type(subjects),'-----------------------',subjects)
            print('programms: ', type(programms),'-----------------------',programms)
            Te.subject.set(subjects)
            Te.program.set(programms)
            return redirect('/teacher/')

    prog = Program.objects.all()
    subj = Subject.objects.all()
    return render(request, 'AddTeachers.html', {'programs':prog, 'subjects': subj})

def Teachers_list(request):
    teach = Teacher.objects.all()
    
    return render(request, 'teacher.html', {'teacher':teach})