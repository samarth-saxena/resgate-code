from portal.models import Lab
import csv


def run():
    with open('csvs/labs.csv') as file:
        reader = csv.reader(file)
        # next(reader)  # Advance past the header

        Lab.objects.all().delete()

        for row in reader:
            print(row)

            _, lab = Lab.objects.get_or_create(name=row[1], website=row[2],)

            # lab.save()