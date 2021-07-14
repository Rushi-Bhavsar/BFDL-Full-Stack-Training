from django.shortcuts import render
from .forms import FirstForm


def index(request):
    return render(request, 'third_app/index.html')


def my_forms(request):
    form_obj = FirstForm()
    if request.method == 'POST':
        form_obj = FirstForm(request.POST)
        if form_obj.is_valid():
            print(form_obj.cleaned_data['name'])
            print(form_obj.cleaned_data['email'])
            print(form_obj.cleaned_data['text'])
    return render(request, 'third_app/forms.html', {'form_key': form_obj})
