from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.


def index(request):
    mydict = {'mylist': "Welcome to first Django Template from template/first_app directory."}
    render_obj = render(request, 'first_app/first_template.html', context=mydict)
    return render_obj


def show_images(request):
    return render(request, 'first_app/image_templates.html')


def show_access_records(request):
    records = AccessRecord.objects.order_by('date')
    my_date_dict = {'data': records}
    return render(request, 'first_app/access_records.html', context=my_date_dict)
