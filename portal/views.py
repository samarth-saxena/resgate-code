from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.http.response import Http404, HttpResponseBase
from django.contrib.auth import authenticate, login, logout
from .forms import StudentSignupForm, ProfessorSignupForm, ProfAddProjectsForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from portal.models import UserProfile, Student, Professor, Lab, Domain, Projects

from .serializers import ProjectSerializer
from scripts.utils import *
from scripts import recommender


# regular functions
def get_projects_dict():
	
	projects = list(Projects.objects.all())
	projects_dict = []
	
	for project in projects:
		ser_proj = ProjectSerializer(project).data
		domains = []
		for domain_id in ser_proj['domains']:
			domains.append(Domain.objects.get(domain_id).title)
		ser_proj['domains'] = domains
		projects_dict.append(ser_proj)
	
	return projects_dict

def get_project_from_dict(projects):
	project_objs = []
	scores = []
	for proj in projects:
		project_objs.append(Projects.objects.get(title=proj[0]['title']))
		scores.append(int(100*(1-proj[1])))
	
	return project_objs, scores

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

def landing(request):
	# return render(request, 'auth/landing.html')
	return redirect_user(request)

def check_student(request):
	if request.user.is_authenticated:
		try:
			user_profile = UserProfile.objects.get(user=request.user)
			return user_profile.is_Student

		except UserProfile.DoesNotExist:
			raise Http404()
	else:
		return False

def check_professor(request):
	if request.user.is_authenticated:
		try:
			user_profile = UserProfile.objects.get(user=request.user)
			return user_profile.is_Professor

		except UserProfile.DoesNotExist:
			raise Http404()
	else:
		return False

def redirect_user(request):
	if request.user.is_authenticated:
		try:
			user_profile = UserProfile.objects.get(user=request.user)
			# if user_profile.is_verified:
			if user_profile.is_Student:
				return redirect('student_home')
			elif user_profile.is_Professor:
				return redirect('prof_home')
			else:
				return redirect('login')
		except UserProfile.DoesNotExist:
			raise Http404()
	else:
		return redirect('login')

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
				return redirect_user(request)

			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="auth/login.html", context={"login_form":form})

def logout_view(request):
	logout(request)
	return redirect('login')

def student_signup(request):
	if request.method == "POST":
		form = StudentSignupForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()
			user.save()
			Student.objects.create(user=user,is_Student=True)
			login(request, user)
			messages.success(request, "Signup successful." )
			return redirect("student_home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = StudentSignupForm()
	return render (request=request, template_name="auth/stud_signup.html", context={"stud_signup_form":form})

def professor_signup(request):
	if request.method == "POST":
		form = ProfessorSignupForm(request.POST)
		if form.is_valid():
			user = form.save()
			Professor.objects.create(user=user,is_Professor=True)
			login(request, user)
			messages.success(request, "Signup successful." )
			return redirect("prof_home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = ProfessorSignupForm()
	return render (request=request, template_name="auth/prof_signup.html", context={"prof_signup_form":form})


def student_home(request):
	if check_student(request):
		# retrieving projects
		projects = get_projects_dict()
		student = Student.objects.get(user=request.user)
		
		final_recs = Projects.objects.all()
		scores = []
		if student.resume is not None:
			student_resume_url = student.resume.url
			rec_projects = recommender.top_picks(pdf_url=student_resume_url,projects=projects)
			final_recs, scores = get_project_from_dict(rec_projects)
		
		context = {
			'recommendations': final_recs,
			'scores': scores
		}
		return render(request, 'students/stud_home.html',context)
	else:
		return redirect_user(request)

def student_browse(request):
	if check_student(request):
		openings = Projects.objects.all()

		return render(request, 'students/stud_browse.html', {
			'name':'student_browse',
			'openings':openings,
			})
	else:
		return redirect_user(request)		

def student_domain(request):
	if check_student(request):
		return render(request, 'students/stud_domain.html', {'name':'student_domain'})
	else:
		return redirect_user(request)

def student_lab(request):
	if check_student(request):
		# labs = []
		labs = Lab.objects.all()
		return render(request, 'students/stud_lab.html', {
			'name':'student_lab',
			'labs': labs,
			})
	else:
		return redirect_user(request)

def student_profile(request):
	if check_student(request):
		return render(request, 'students/stud_profile.html', {'name':'student_profile'})
	else:
		return redirect_user(request)


# PROFESSOR
def prof_home(request):
	if check_professor(request):
		return render(request, 'professors/prof_home.html')
	else:
		return redirect_user(request)

def prof_projects(request):
	# return HttpResponse("Listings of all current projects, and add new projects")
	if check_professor(request):
		form = ProfAddProjectsForm()

		return render(request, 'professors/prof_projects.html',{'form':form})
	else:
		return redirect_user(request)

def prof_students(request):
	# return HttpResponse("Listings of all current students working")
	if check_professor(request):
		return render(request, 'professors/prof_students.html')
	else:
		return redirect_user(request)

def prof_profile(request):
	# return HttpResponse("Listings of all current projects, and add new projects")
	if check_professor(request):
		return render(request, 'professors/prof_profile.html')
	else:
		return redirect_user(request)

def prof_addproject(request):
	if check_professor(request):
		# if this is a POST request we need to process the form data
		if request.method == 'POST':
			# create a form instance and populate it with data from the request:
			form = ProfAddProjectsForm(request.POST,request.FILES)
			# check whether it's valid:
			if form.is_valid():
				project = form.save()
				project.save()

				# process the data in form.cleaned_data as required
				# ...
				# redirect to a new URL:
				return redirect('admin_products')

		# if a GET (or any other method) we'll create a blank form
			# remove
		# else:
			# add line in admin products
			# form = AdminAddProductsForm()

		# return render(request, 'admin/name.html', {'form': form})
		return prof_projects(request)
	else:
		return redirect_user(request)