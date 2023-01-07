from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('student_home')
        else:
            # Return an 'invalid login' error message.
            ...
    else:
        return render(request, 'auth/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def signup_view(request):
    return render(request, 'auth/signup.html')

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

