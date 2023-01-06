from django.db import models

# Create your models here.
class Student(models.Model):
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
    #Student_CV

class StudentCV(models.Model):
    file = models.FileField(upload_to='uploads/%Y/%m/%d/')

class Lab(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField(max_length=300)

class Domain(models.Model):
    title = models.CharField(max_length=255)

class Professor(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length = 254)
    #lab = Lab
    #professor (one lab can have many prof, but one prof can have 1 lab only)
    website = models.URLField(max_length=300)

class Openings(models.Model):
    #lab = Lab (one lab can have many openings)
    #professor = Professor (one opening can only have many professor)
    #domain = Domain
    description = models.TextField()

    OPEN = 'O'
    CLOSED = 'C'
    STATUS_CHOICES = [
        (OPEN, 'Open'),
        (CLOSED, 'Closed'),
    ]
    status = models.CharField(max_length=1,choices=STATUS_CHOICES,default=OPEN)    

class Application(models.Model):
    #student = Student
    #opening = Opening (each opening can have multiple applications)
    openingDate = models.DateField()
    updateDate = models.DateField()
    #student_cv = Student_CV

    PENDING = 'P'
    REJECTED = 'R'
    ACCEPTED = 'A'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (REJECTED, 'Rejected'),
        (ACCEPTED, 'Accepted'),
    ]
    status = models.CharField(max_length=1,choices=STATUS_CHOICES,default=PENDING)



