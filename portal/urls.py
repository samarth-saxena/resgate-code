from django.urls import path

from . import views

urlpatterns = [
    path('hello/', views.say_hello, name='index'),

	path('',views.student_home, name='student_home'),
	path('browse/',views.student_browse, name='student_browse'),

	path('prof/',views.prof_home, name='prof_home'), # recommended applications
	path('prof/students',views.prof_students, name='prof_students'), # current students
	path('prof/projects',views.prof_projects, name='prof_projects'), # my openings, add new openings


]