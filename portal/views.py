from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('student_home')
#         else:
#             # Return an 'invalid login' error message.
#             ...
#     else:
#         return render(request, 'auth/login.html')

def login_view(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, "You are now logged in as {username}.")
				return redirect("student_home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="auth/login.html", context={"login_form":form})

def logout_view(request):
    logout(request)
    return redirect('login')

# def signup_view(request):
#     return render(request, 'auth/signup.html')

def signup_view(request):
	if request.method == "POST":
		form = SignupForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Signup successful." )
			return redirect("student_home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = SignupForm()
	return render (request=request, template_name="auth/signup.html", context={"signup_form":form})

def student_home(request):
	return render(request, 'students/stud_home.html')

def student_browse(request):
	return render(request, 'students/stud_browse.html', {'name':'student_browse'})

def student_domain(request):
	return render(request, 'students/stud_domain.html', {'name':'student_domain'})

def student_lab(request):
	return render(request, 'students/stud_lab.html', {'name':'student_lab'})

def prof_home(request):
	return render(request, 'professors/prof_home.html')

def prof_projects(request):
	# return HttpResponse("Listings of all current projects, and add new projects")
	return render(request, 'professors/prof_projects.html')


def prof_students(request):
	# return HttpResponse("Listings of all current students working")
	return render(request, 'professors/prof_students.html')

