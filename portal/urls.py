from django.urls import path

from . import views

urlpatterns = [
	path('login/', views.login_view, name='login'),
	path('signup/', views.signup_view, name='signup'),

	path('',views.student_home, name='student_home'),
	path('browse/',views.student_browse, name='student_browse'),

	path('prof/',views.prof_home, name='prof_home'), # recommended applications
	path('prof/students',views.prof_students, name='prof_students'), # current students
	path('prof/projects',views.prof_projects, name='prof_projects'), # my openings, add new openings


]