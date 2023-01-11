from django.db import models
# from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Custom user
# name
# email
class UserProfile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,blank=False,null=True)
	# name = models.CharField(max_length=60)
	# email = models.EmailField(max_length = 254)
	is_Student = models.BooleanField(default=False)
	is_Professor = models.BooleanField(default=False)
	

	def __str__(self):
		return self.user.username

# Create your models here.
class Student(UserProfile):


	BTECH = 'B'
	MTECH = 'M'
	PHD = 'P'
	PROGRAM_CHOICES = [
		(BTECH, 'BTech'),
		(MTECH, 'MTech'),
		(PHD, 'PhD'),
	]
	program = models.CharField(max_length=1,choices=PROGRAM_CHOICES,default=BTECH) 

	CSE = 'CSE'
	CSD = 'CSD'
	CSB = 'CSB'
	CSSS = 'CSSS'
	CSAI = 'CSAI'
	ECE = 'ECE'
	EEE = 'EEE'
	CB = 'CB'
	BRANCH_CHOICES = [
		(CSE, 'CSE'),
		(CSD, 'CSD'),
		(CSB, 'CSB'),
		(CSSS, 'CSSS'),
		(CSAI, 'CSAI'),
		(ECE, 'ECE'),
		(EEE, 'EEE'),
		(CB, 'CB'),
	]
	BATCH_CHOICES = [
		(2019,'2019'),
		(2020,'2020'),
		(2021,'2021'),
		(2022,'2022'),
	]
	branch = models.CharField(max_length=4,choices=BRANCH_CHOICES,default=CSE) 

	batch = models.IntegerField(default=2022, choices = BATCH_CHOICES)
	tags = models.JSONField(null=True,blank=True)
	resume = models.FileField(upload_to='resumes/%Y/%m/%d/',null=True,blank=True)

	def __str__(self):
		return self.user.username
	
# class Resume(models.Model):
# 	file = models.FileField(upload_to='uploads/%Y/%m/%d/')
# 	student = models.ForeignKey(Student, related_name='resumes', on_delete=models.CASCADE)

# 	def __str__(self):
# 		return "Resume " + self.student.__str__()

class Lab(models.Model):
	name = models.CharField(max_length=100)
	website = models.URLField(max_length=300)

	def __str__(self):
		return self.name

class Domain(models.Model):
	title = models.CharField(max_length=255)
	
	def __str__(self):
		return self.title

class Projects(models.Model):
	title = models.TextField(max_length=300,null=True)
	description = models.TextField(max_length=5000)
	available = models.BooleanField()
	domain = models.ManyToManyField(Domain, related_name='projects')
	skills = models.TextField(max_length=1000,null=True,blank=True)
	# TODO add domaon, skills to prof_projects.html
	
	# OPEN = 'O'
	# CLOSED = 'C'
	# STATUS_CHOICES = [
	# 	(OPEN, 'Open'),
	# 	(CLOSED, 'Closed'),
	# ]
	# status = models.CharField(max_length=1,choices=STATUS_CHOICES,default=OPEN)    #BooleanField().

	def __str__(self):
		return self.title

class Professor(UserProfile):
	website = models.URLField(max_length=300)
	interests = models.JSONField(null=True)

	lab = models.ForeignKey(Lab, related_name='profs', on_delete=models.SET_NULL,blank=False,null=True)
	projects = models.ManyToManyField(Projects, related_name='profs')

	def __str__(self):
		return self.user.username

class Application(models.Model):
	openingDate = models.DateField()
	student = models.ForeignKey(Student, related_name='applications', on_delete=models.CASCADE,blank=False,null=True)
	project = models.ForeignKey(Projects, related_name='applications', on_delete=models.CASCADE,blank=False,null=True)
	# resume = models.ForeignKey(Resume, related_name='applications', on_delete=models.CASCADE,blank=False,null=True)

	PENDING = 'P'
	REJECTED = 'R'
	ACCEPTED = 'A'
	STATUS_CHOICES = [
		(PENDING, 'Pending'),
		(REJECTED, 'Rejected'),
		(ACCEPTED, 'Accepted'),
	]
	status = models.CharField(max_length=1,choices=STATUS_CHOICES,default=PENDING)

	def __str__(self):
		return self.student.__str() + " - " + self.project.__str()