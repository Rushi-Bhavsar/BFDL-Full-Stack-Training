import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')
import django
django.setup()
from first_app.models import *
from faker import Faker
import random

fake = Faker()

topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(n=5):
    for entry in range(n):

        # Create Topic name.
        top = add_topic()

        # Create Fake records.
        fake_url = fake.url()
        fake_date = fake.date()
        fake_name = fake.company()

        # Add Fake records to WebPage table.
        web_pg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        # Add Fake records to AccessRecords table.
        acc_record = AccessRecord.objects.get_or_create(name=web_pg, date=fake_date)[0]


print("Populating Scripts!!")
populate(20)
print("Population complete.")
