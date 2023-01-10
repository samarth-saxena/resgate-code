from django.contrib.auth.models import User
from portal.models import UserProfile, Professor, Domain
from django.contrib.auth.hashers import make_password

import csv


def run():
	with open('csvs/profs_domains.csv') as file:
		reader = csv.reader(file)
		next(reader)  # Advance past the header

		Domain.objects.all().delete()
		Professor.objects.all().delete()

		i=0
		for row in reader:
			print(row)

			domain, _ = Domain.objects.get_or_create(title=row[0])

			userobj, created = User.objects.get_or_create(username=row[1],email="prof@gmail.com",password=make_password("alpha101"))
			# user.save()
			if created:
				stud = Professor(user=userobj, is_Professor=True, website="www.iiitd.ac.in")
				stud.save()
				i = i+1
			# stud.save()

			# lab.save()