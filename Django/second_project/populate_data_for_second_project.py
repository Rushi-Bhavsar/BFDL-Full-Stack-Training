import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'second_project.settings')
import django
django.setup()
from second_app.models import Users
from faker import Faker


def populate(n=5):
    for entry in range(n):
        fake = Faker()
        fake_first_name = fake.first_name()
        fake_last_name = fake.last_name()
        fake_email = fake.email()

        user = Users.objects.get_or_create(FirstName=fake_first_name, LastName=fake_last_name, Email=fake_email)[0]
        user.save()


print("Populating Data!!!")
populate(30)
print("Population completed.")
