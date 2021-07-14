from django.shortcuts import render


def index(request):
    return render(request, 'fourth_app/index.html')


def other(request):
    return render(request, 'fourth_app/other.html')


def relative_url(request):
    return render(request, 'fourth_app/relative_urls_templates.html')
