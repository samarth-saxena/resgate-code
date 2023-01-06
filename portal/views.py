from django.shortcuts import render
from django.http import HttpResponse

def student_home(request):
	return render(request, 'students/stud_home.html')

def student_browse(request):
	return render(request, 'students/stud_browse.html', {'name':'student_browse'})

def prof_home(request):
	return render(request, 'professors/prof_home.html')

def prof_projects(request):
	# return HttpResponse("Listings of all current projects, and add new projects")
	return render(request, 'professors/prof_projects.html')


def prof_students(request):
	# return HttpResponse("Listings of all current students working")
	return render(request, 'professors/prof_students.html')
