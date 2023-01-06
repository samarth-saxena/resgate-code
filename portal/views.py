from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def say_hello(request):
# 	return HttpResponse("Hello world!!")


def say_hello(request):
	return render(request, 'hello.html', {'name':'Sam'})

def student_home(request):
	return render(request, 'students/stud_home.html')

def student_browse(request):
	return HttpResponse("Browse")

def prof_home(request):
	return HttpResponse("Prof home: View recommended and new applications")

def prof_projects(request):
	return HttpResponse("Listings of all current projects, and add new projects")

def prof_students(request):
	return HttpResponse("Listings of all current students working")