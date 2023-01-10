from django.contrib.auth.models import User
from portal.models import UserProfile, Student, Professor
from django.contrib.auth.hashers import make_password
import csv


def run():
    # with open('csvs/labs.csv') as file:
    #     reader = csv.reader(file)
    #     # next(reader)  # Advance past the header

    #     Lab.objects.all().delete()

    #     for row in reader:
    #         print(row)

    #         _, lab = Lab.objects.get_or_create(name=row[1], website=row[2],)

    #         # lab.save()
	Student.objects.all().delete()
	User.objects.all().exclude(username="admin").delete()
	for i in range(1,11):
		user = User(username="Stud"+str(i),email="stud"+str(i)+"@gmail.com",password=make_password("alpha101"))
		user.save()

		stud = Student(user=user, is_Student=True, resume="")
		stud.save()
