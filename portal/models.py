from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom user
# name
# email


# Create your models here.
class Student(AbstractUser):
	name = models.CharField(max_length=60)

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
	branch = models.CharField(max_length=4,choices=BRANCH_CHOICES,default=CSE) 

	batch = models.IntegerField(default=2022)
	email = models.EmailField(max_length = 254)
	tags = models.JSONField()
	
class Resume(models.Model):
	file = models.FileField(upload_to='uploads/%Y/%m/%d/')
	student = models.ForeignKey(Student, related_name='resumes')

class Lab(models.Model):
	name = models.CharField(max_length=100)
	website = models.URLField(max_length=300)

class Domain(models.Model):
	title = models.CharField(max_length=255)


class Projects(models.Model):
	description = models.TextField(max_length=5000)
	available = models.BooleanField()
	domain = models.ManyToManyField(Domain, related_name='projects')

	# OPEN = 'O'
	# CLOSED = 'C'
	# STATUS_CHOICES = [
	# 	(OPEN, 'Open'),
	# 	(CLOSED, 'Closed'),
	# ]
	# status = models.CharField(max_length=1,choices=STATUS_CHOICES,default=OPEN)    #BooleanField().

class Professor(AbstractUser):
	name = models.CharField(max_length=60)
	email = models.EmailField(max_length = 254)
	website = models.URLField(max_length=300)
	interests = models.TextField(max_length=2000)

	lab = models.ForeignKey(Lab, related_name='profs', on_delete=models.SET_NULL,blank=True,null=True)
	projects = models.ManyToManyField(Projects, related_name='profs')


class Application(models.Model):
	openingDate = models.DateField()
	student = models.ForeignKey(Student, related_name='applications')
	project = models.ForeignKey(Projects, related_name='applications')
	resume = models.ForeignKey(Resume, related_name='applications')

	PENDING = 'P'
	REJECTED = 'R'
	ACCEPTED = 'A'
	STATUS_CHOICES = [
		(PENDING, 'Pending'),
		(REJECTED, 'Rejected'),
		(ACCEPTED, 'Accepted'),
	]
	status = models.CharField(max_length=1,choices=STATUS_CHOICES,default=PENDING)