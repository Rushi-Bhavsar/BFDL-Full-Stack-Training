from django.shortcuts import render
from .forms import UserFrom


def index(request):
    return render(request, 'second_app/index.html')


def users(request):
    form_obj = UserFrom()
    if request.method == 'POST':
        form_obj = UserFrom(request.POST)

        if form_obj.is_valid():
            form_obj.save(commit=True)
            return index(request)
        else:
            print('Error Form is valid.')

    return render(request, 'second_app/user_records.html', {'form_key': form_obj})
