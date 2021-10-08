from django.urls import path, include
from quiz import views
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [

    path('student/', include('student.urls')),
    path('teacher/', include('teacher.urls')),

    path('', views.home_view, name=''),
    path('logout', LogoutView.as_view(template_name='quiz/logout.html'), name='logout'),
    path('afterlogin', views.afterlogin_view, name='afterlogin'),

    path('teacherclick', views.teacherclick_view),
    path('teacherlogin', LoginView.as_view(template_name='quiz/teacherlogin.html'), name='teacherlogin'),
    path('teacher-dashboard', views.teacher_dashboard_view, name='teacher-dashboard'),
    path('teacher-student', views.teacher_student_view, name='teacher-student'),
    path('teacher-view-student', views.teacher_view_student_view, name='teacher-view-student'),
    path('teacher-view-student-marks', views.teacher_view_student_marks_view, name='teacher-view-student-marks'),
    path('teacher-view-marks/<int:pk>', views.teacher_view_marks_view, name='teacher-view-marks'),
    path('teacher-check-marks/<int:pk>', views.teacher_check_marks_view, name='teacher-check-marks'),
    path('update-student/<int:pk>', views.update_student_view, name='update-student'),
    path('delete-student/<int:pk>', views.delete_student_view, name='delete-student'),

    path('teacher-course', views.teacher_course_view, name='teacher-course'),
    path('teacher-add-course', views.teacher_add_course_view, name='teacher-add-course'),
    path('teacher-view-course', views.teacher_view_course_view, name='teacher-view-course'),
    path('delete-course/<int:pk>', views.delete_course_view, name='delete-course'),

    path('teacher-question', views.teacher_question_view, name='teacher-question'),
    path('teacher-add-question', views.teacher_add_question_view, name='teacher-add-question'),
    path('teacher-view-question', views.teacher_view_question_view, name='teacher -view-question'),
    path('view-question/<int:pk>', views.view_question_view, name='view-question'),
    path('delete-question/<int:pk>', views.delete_question_view, name='delete-question'),

]
