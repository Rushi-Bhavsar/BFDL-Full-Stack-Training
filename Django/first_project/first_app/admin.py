from django.contrib import admin
from .models import Topic, AccessRecord, Webpage
# Register your models here.

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
