from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.http import HttpResponse

from .models import Student, Challenge

import ClassroomBot.classroombot

menu = ['info', 'students', 'admin-panel']

def index(request):
    return HttpResponse('Hello, World!')

def user_check(request):
    highest_week = Challenge.objects.count()
    student_list = Student.objects.all()

    lowest_week = 0

    for student in Student.objects.all():
        if student.completed_weeks < highest_week:
            highest_week = student.completed_weeks
            lowest_week = student.completed_weeks


    print(lowest_week, "weeks completed as a class")
    current_challenge = Challenge.objects.order_by('week_number')[lowest_week]

    project_number = "%02d" % current_challenge.week_number

    context = {'student_list' : student_list, 'current_challenge' : current_challenge, 'project_number' : project_number, 'menu' : menu}
    return render(request, 'polls/index.html', context)

def display_students(request):
    student_list = Student.objects.all()

    for student in student_list:
        student.project_list = []
        print(student)
        if student.completed_weeks:
            for week_number in range(1,student.completed_weeks+1):
                project_name = "http://repl.it/@%s/week%02d" % (student.student_name, week_number)
                student.project_list.append(project_name)

        else:
            student.project_list = ["none"]
        print(student, student.project_list)
    week_number = 10

    project_overview = range(week_number,week_number-3,-1)
    p = [i for i in range(week_number, week_number-3, -1)]

    context = {'student_list' : student_list, 'text' : 'Student Lists with project links!', 'menu': menu, 'project_overview': project_overview, 'p': p}

    return render(request, 'polls/students.html', context)

def update_users(request):

    # if student check fails. ask for a "beta" variable, so there i a link to in production!

    highest_week = Challenge.objects.count()

    print("updating users..")

    for student in Student.objects.all():
        s = student

        print("updating info for",student.student_name)
        week_count, week_beta = ClassroomBot.classroombot.main(student.student_name, last_known_week = s.completed_weeks, classroom_total_weeks = highest_week)
        print(student.student_name,"has completed",week_count,"weeks!")
        if s.completed_weeks == week_count:
            continue
        s.completed_weeks = week_count
        s.current_week_in_progress = week_beta
        s.save()

    context = {'text':"All Your Progress Are Belong To Us", 'menu' : menu}

    return render(request, 'polls/update.html', context)

def reset_users_progress(request):

    for student in Student.objects.all():
        s = student
        s.completed_weeks = 0
        s.current_week_in_progress = False
        s.save()

    context = {'text':"All Users' Progress Reset", 'menu' : menu}
    return render(request, 'polls/update.html', context)

def redirect(request):
    context = {'text':"You're Looking for the main page", 'menu' : menu}
    return render(request, 'polls/update.html', context)

def admin_panel(request):
    context = {'text':"Semi Admin Panel", 'menu' : menu}
    return render(request, 'polls/admin-panel.html', context)

def info(request):
    context = {'text':"Info About nerdPuzzles.ca", 'menu' : menu}
    return render(request, 'polls/info.html', context)
