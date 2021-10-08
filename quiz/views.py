from django.shortcuts import render, redirect, reverse
from . import forms, models
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.conf import settings
from django.db.models import Q
from django.core.mail import send_mail
from teacher import models as TMODEL
from student import models as SMODEL
from teacher import forms as TFORM
from student import forms as SFORM
from django.contrib.auth.models import User
from quiz import forms as QFORM


def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request, 'quiz/index.html')


def is_teacher(user):
    return user.groups.filter(name='TEACHER').exists()


def is_student(user):
    return user.groups.filter(name='STUDENT').exists()


def afterlogin_view(request):
    if is_student(request.user):
        return redirect('student/student-dashboard')
    elif is_teacher(request.user):
        accountapproval = TMODEL.Teacher.objects.all().filter(user_id=request.user.id, status=True)
        if accountapproval:
            return redirect('teacher/teacher-dashboard')
    else:
        return redirect('teacher-dashboard')

def teacherclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return HttpResponseRedirect('teacherlogin')


@login_required(login_url='teacherlogin')
def teacher_dashboard_view(request):
    dict = {
        'total_student': SMODEL.Student.objects.all().count(),
        'total_teacher': TMODEL.Teacher.objects.all().filter(status=True).count(),
        'total_course': models.Course.objects.all().count(),
        'total_question': models.Question.objects.all().count(),
    }
    return render(request, 'quiz/teacher_dashboard.html', context=dict)


@login_required(login_url='teacherlogin')
def update_student_view(request, pk):
    student = SMODEL.Student.objects.get(id=pk)
    user = SMODEL.User.objects.get(id=student.user_id)
    userForm = SFORM.StudentUserForm(instance=user)
    studentForm = SFORM.StudentForm(request.FILES, instance=student)
    mydict = {'userForm': userForm, 'studentForm': studentForm}
    if request.method == 'POST':
        userForm = SFORM.StudentUserForm(request.POST, instance=user)
        studentForm = SFORM.StudentForm(request.POST, request.FILES, instance=student)
        if userForm.is_valid() and studentForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            studentForm.save()
            return redirect('teacher-view-student')
    return render(request, 'quiz/update_student.html', context=mydict)


@login_required(login_url='teacherlogin')
def delete_student_view(request, pk):
    student = SMODEL.Student.objects.get(id=pk)
    user = User.objects.get(id=student.user_id)
    user.delete()
    student.delete()
    return HttpResponseRedirect('/teacher-view-student')


@login_required(login_url='teacherlogin')
def teacher_course_view(request):
    return render(request, 'quiz/teacher_course.html')


@login_required(login_url='teacherlogin')
def teacher_add_course_view(request):
    courseForm = forms.CourseForm()
    if request.method == 'POST':
        courseForm = forms.CourseForm(request.POST)
        if courseForm.is_valid():
            courseForm.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect('/teacher-view-course')
    return render(request, 'quiz/teacher_add_course.html', {'courseForm': courseForm})


@login_required(login_url='teacherlogin')
def teacher_view_course_view(request):
    courses = models.Course.objects.all()
    return render(request, 'quiz/teacher_view_course.html', {'courses': courses})


@login_required(login_url='teacherlogin')
def delete_course_view(request, pk):
    course = models.Course.objects.get(id=pk)
    course.delete()
    return HttpResponseRedirect('/teacher-view-course')


@login_required(login_url='teacherlogin')
def teacher_question_view(request):
    return render(request, 'quiz/teacher_question.html')


@login_required(login_url='teacherlogin')
def teacher_add_question_view(request):
    questionForm=forms.QuestionForm()
    if request.method=='POST':
        questionForm=forms.QuestionForm(request.POST)
        if questionForm.is_valid():
            question=questionForm.save(commit=False)
            course=models.Course.objects.get(id=request.POST.get('courseID'))
            question.course=course
            question.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect('/teacher-view-question')
    return render(request,'quiz/teacher_add_question.html',{'questionForm':questionForm})


@login_required(login_url='teacherlogin')
def teacher_view_question_view(request):
    courses = models.Course.objects.all()
    return render(request, 'quiz/teacher_view_question.html', {'courses': courses})


@login_required(login_url='teacherlogin')
def view_question_view(request, pk):
    questions = models.Question.objects.all().filter(course_id=pk)
    return render(request, 'quiz/view_question.html', {'questions': questions})


@login_required(login_url='teacherlogin')
def delete_question_view(request, pk):
    question = models.Question.objects.get(id=pk)
    question.delete()
    return HttpResponseRedirect('/teacher-view-question')


@login_required(login_url='teacherlogin')
def teacher_view_student_marks_view(request):
    students = SMODEL.Student.objects.all()
    return render(request, 'quiz/teacher_view_student_marks.html', {'students': students})


@login_required(login_url='teacherlogin')
def teacher_view_marks_view(request, pk):
    courses = models.Course.objects.all()
    response = render(request, 'quiz/teacher_view_marks.html', {'courses': courses})
    response.set_cookie('student_id', str(pk))
    return response


@login_required(login_url='teacherlogin')
def teacher_check_marks_view(request, pk):
    course = models.Course.objects.get(id=pk)
    student_id = request.COOKIES.get('student_id')
    student = SMODEL.Student.objects.get(id=student_id)

    results = models.Result.objects.all().filter(exam=course).filter(student=student)
    return render(request, 'quiz/teacher_check_marks.html', {'results': results})


def aboutus_view(request):
    return render(request, 'quiz/aboutus.html')


def contactus_view(request):
    sub = forms.ContactusForm()
    if request.method == 'POST':
        sub = forms.ContactusForm(request.POST)
        if sub.is_valid():
            email = sub.cleaned_data['Email']
            name = sub.cleaned_data['Name']
            message = sub.cleaned_data['Message']
            send_mail(str(name) + ' || ' + str(email), message, settings.EMAIL_HOST_USER, settings.EMAIL_RECEIVING_USER,
                      fail_silently=False)
            return render(request, 'quiz/contactussuccess.html')
    return render(request, 'quiz/contactus.html', {'form': sub})


@login_required(login_url='teacherlogin')
def teacher_student_view(request):
    dict={
    'total_student':SMODEL.Student.objects.all().count(),
    }
    return render(request,'quiz/teacher_student.html',context=dict)

@login_required(login_url='teacherlogin')
def teacher_view_student_view(request):
    students= SMODEL.Student.objects.all()
    return render(request,'quiz/teacher_view_student.html',{'students':students})

@login_required(login_url='teacherlogin')
def teacher_add_course(request):
    courseForm=forms.CourseForm()
    if request.method=='POST':
        courseForm=forms.CourseForm(request.POST)
        if courseForm.is_valid():
            courseForm.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect('/teacher-view-course')
    return render(request,'quiz/teacher_add_course.html',{'courseForm':courseForm})

