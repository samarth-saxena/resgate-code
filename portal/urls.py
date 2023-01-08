from django.urls import path

from . import views

urlpatterns = [
	path('', views.landing, name='landing'),
	path('login/', views.login_view, name='login'),
	path('signup/student', views.student_signup, name='student_signup'),
	path('signup/professor', views.professor_signup, name='prof_signup'),
	path('logout/', views.logout_view, name='logout'),
	
	path('student/',views.student_home, name='student_home'),
	path('student/browse/',views.student_browse, name='student_browse'),
	path('student/domain/',views.student_domain, name='student_domain'),
	path('student/lab/',views.student_lab, name='student_lab'),
	path('student/profile/',views.student_profile, name='student_profile'),

	path('professor/',views.prof_home, name='prof_home'), # recommended applications
	path('professor/students',views.prof_students, name='prof_students'), # current students
	path('professor/projects',views.prof_projects, name='prof_projects'), # my openings, add new openings
	path('professor/profile',views.prof_profile, name='prof_profile'), # my openings, add new openings
	path('professor/addproject',views.prof_addproject, name='prof_addproject'), # my openings, add new openings
]