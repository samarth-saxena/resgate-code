from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=60)
    program = models.CharField(max_length=10) #btech, mtech, phd Make choices?
    branch = models.CharField(max_length=10) #cse, csd, ece, csb,etc Make choices?
    batch = models.IntegerField(default=0)
    email = models.EmailField(max_length = 254)
    tags = models.JSONField()
    #Student_CV

class Professor(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length = 254)
    #lab = Lab
    website = models.URLField(max_length=300)

class Lab(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField(max_length=300)
    #professor (one lab can have many prof, but one prof can have 1 lab only)

class Openings(models.Model):
    #lab = Lab (one lab can have many openings)
    #professor = Professor (one opening can only have many professor)
    #domain = Domain
    description = models.TextField()
    status = models.CharField(max_length=10)    #open or close Make choices?

class Domain(models.Model):
    title = models.CharField(max_length=255)

class Application(models.Model):
    #student = Student
    #opening = Opening (each opening can have multiple applications)
    openingDate = models.DateField()
    updateDate = models.DateField()
    #student_cv = Student_CV
    status = models.CharField(max_length=10) #pending, rejected, accepted Make choices?

class StudentCV(models.Model):
    #student = Student
    file = models.FileField(upload_to='uploads/%Y/%m/%d/')










    def __str__(self):
        return self.address1 + self.address2 + self.country